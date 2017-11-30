import pytest

import itertools
import os

from buildstream._artifactcache import ArtifactCacheSpec, configured_remote_artifact_cache_specs
from buildstream._context import Context
from buildstream._project import Project
from buildstream.utils import _deduplicate
from buildstream import _yaml


cache1 = ArtifactCacheSpec(url='https://example.com/cache1', push=True)
cache2 = ArtifactCacheSpec(url='https://example.com/cache2', push=False)
cache3 = ArtifactCacheSpec(url='https://example.com/cache3', push=False)
cache4 = ArtifactCacheSpec(url='https://example.com/cache4', push=False)
cache5 = ArtifactCacheSpec(url='https://example.com/cache5', push=False)
cache6 = ArtifactCacheSpec(url='https://example.com/cache6', push=True)


# Generate cache configuration fragments for the user config and project config files.
#
def configure_remote_caches(override_caches, project_caches=[], user_caches=[]):
    user_config = {}
    if len(user_caches) == 1:
        user_config['artifacts'] = {
            'url': user_caches[0].url,
            'push': user_caches[0].push,
        }
    elif len(user_caches) > 1:
        user_config['artifacts'] = [
            {'url': cache.url, 'push': cache.push} for cache in user_caches
        ]

    if len(override_caches) == 1:
        user_config['projects'] = {
            'test': {
                'artifacts': {
                    'url': override_caches[0].url,
                    'push': override_caches[0].push,
                }
            }
        }
    elif len(override_caches) > 1:
        user_config['projects'] = {
            'test': {
                'artifacts': [
                    {'url': cache.url, 'push': cache.push} for cache in override_caches
                ]
            }
        }

    project_config = {}
    if len(project_caches) > 0:
        if len(project_caches) == 1:
            project_config.update({
                'artifacts': {
                    'url': project_caches[0].url,
                    'push': project_caches[0].push,
                }
            })
        elif len(project_caches) > 1:
            project_config.update({
                'artifacts': [
                    {'url': cache.url, 'push': cache.push} for cache in project_caches
                ]
            })

    return user_config, project_config


# Test that parsing the remote artifact cache locations produces the
# expected results.
@pytest.mark.parametrize(
    'override_caches, project_caches, user_caches',
    [
        # The leftmost cache is the highest priority one in all cases here.
        pytest.param([], [], [], id='empty-config'),
        pytest.param([], [], [cache1, cache2], id='user-config'),
        pytest.param([], [cache1, cache2], [cache3], id='project-config'),
        pytest.param([cache1], [cache2], [cache3], id='project-override-in-user-config'),
        pytest.param([cache1, cache2], [cache3, cache4], [cache5, cache6], id='list-order'),
        pytest.param([cache1, cache2, cache1], [cache2], [cache2, cache1], id='duplicates'),
    ])
def test_artifact_cache_precedence(tmpdir, override_caches, project_caches, user_caches):
    # Produce a fake user and project config with the cache configuration.
    user_config, project_config = configure_remote_caches(override_caches, project_caches, user_caches)
    project_config['name'] = 'test'

    user_config_file = tmpdir.join('buildstream.conf')
    _yaml.dump(_yaml.node_sanitize(user_config), filename=user_config_file)

    project_dir = tmpdir.mkdir('project')
    project_config_file = project_dir.join('project.conf')
    _yaml.dump(_yaml.node_sanitize(project_config), filename=project_config_file)

    context = Context([])
    context.load(config=user_config_file)
    project = Project(project_dir, context)

    # Use the helper from the artifactcache module to parse our configuration.
    parsed_cache_specs = configured_remote_artifact_cache_specs(context, project)

    # Verify that it was correctly read.
    expected_cache_specs = list(_deduplicate(itertools.chain(override_caches, project_caches, user_caches)))
    assert parsed_cache_specs == expected_cache_specs