# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from buildstream._protos.build.buildgrid import local_cas_pb2 as build_dot_buildgrid_dot_local__cas__pb2


class LocalContentAddressableStorageStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FetchMissingBlobs = channel.unary_unary(
                '/build.buildgrid.LocalContentAddressableStorage/FetchMissingBlobs',
                request_serializer=build_dot_buildgrid_dot_local__cas__pb2.FetchMissingBlobsRequest.SerializeToString,
                response_deserializer=build_dot_buildgrid_dot_local__cas__pb2.FetchMissingBlobsResponse.FromString,
                )
        self.UploadMissingBlobs = channel.unary_unary(
                '/build.buildgrid.LocalContentAddressableStorage/UploadMissingBlobs',
                request_serializer=build_dot_buildgrid_dot_local__cas__pb2.UploadMissingBlobsRequest.SerializeToString,
                response_deserializer=build_dot_buildgrid_dot_local__cas__pb2.UploadMissingBlobsResponse.FromString,
                )
        self.FetchTree = channel.unary_unary(
                '/build.buildgrid.LocalContentAddressableStorage/FetchTree',
                request_serializer=build_dot_buildgrid_dot_local__cas__pb2.FetchTreeRequest.SerializeToString,
                response_deserializer=build_dot_buildgrid_dot_local__cas__pb2.FetchTreeResponse.FromString,
                )
        self.UploadTree = channel.unary_unary(
                '/build.buildgrid.LocalContentAddressableStorage/UploadTree',
                request_serializer=build_dot_buildgrid_dot_local__cas__pb2.UploadTreeRequest.SerializeToString,
                response_deserializer=build_dot_buildgrid_dot_local__cas__pb2.UploadTreeResponse.FromString,
                )
        self.StageTree = channel.stream_stream(
                '/build.buildgrid.LocalContentAddressableStorage/StageTree',
                request_serializer=build_dot_buildgrid_dot_local__cas__pb2.StageTreeRequest.SerializeToString,
                response_deserializer=build_dot_buildgrid_dot_local__cas__pb2.StageTreeResponse.FromString,
                )
        self.CaptureTree = channel.unary_unary(
                '/build.buildgrid.LocalContentAddressableStorage/CaptureTree',
                request_serializer=build_dot_buildgrid_dot_local__cas__pb2.CaptureTreeRequest.SerializeToString,
                response_deserializer=build_dot_buildgrid_dot_local__cas__pb2.CaptureTreeResponse.FromString,
                )
        self.CaptureFiles = channel.unary_unary(
                '/build.buildgrid.LocalContentAddressableStorage/CaptureFiles',
                request_serializer=build_dot_buildgrid_dot_local__cas__pb2.CaptureFilesRequest.SerializeToString,
                response_deserializer=build_dot_buildgrid_dot_local__cas__pb2.CaptureFilesResponse.FromString,
                )
        self.GetInstanceNameForRemote = channel.unary_unary(
                '/build.buildgrid.LocalContentAddressableStorage/GetInstanceNameForRemote',
                request_serializer=build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemoteRequest.SerializeToString,
                response_deserializer=build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemoteResponse.FromString,
                )
        self.GetInstanceNameForRemotes = channel.unary_unary(
                '/build.buildgrid.LocalContentAddressableStorage/GetInstanceNameForRemotes',
                request_serializer=build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemotesRequest.SerializeToString,
                response_deserializer=build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemotesResponse.FromString,
                )
        self.GetLocalDiskUsage = channel.unary_unary(
                '/build.buildgrid.LocalContentAddressableStorage/GetLocalDiskUsage',
                request_serializer=build_dot_buildgrid_dot_local__cas__pb2.GetLocalDiskUsageRequest.SerializeToString,
                response_deserializer=build_dot_buildgrid_dot_local__cas__pb2.GetLocalDiskUsageResponse.FromString,
                )


class LocalContentAddressableStorageServicer(object):
    """Missing associated documentation comment in .proto file"""

    def FetchMissingBlobs(self, request, context):
        """Fetch blobs from a remote CAS to the local cache.

        This request is equivalent to ByteStream `Read` or `BatchReadBlobs`
        requests, storing the downloaded blobs in the local cache.

        Requested blobs that failed to be downloaded will be listed in the
        response.

        Errors:
        * `INVALID_ARGUMENT`: The client attempted to download more than the
        server supported limit.

        Individual requests may return the following error, additionally:
        * `NOT_FOUND`: The requested blob is not present in the remote CAS.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadMissingBlobs(self, request, context):
        """Upload blobs from the local cache to a remote CAS.

        This request is equivalent to `FindMissingBlobs` followed by
        ByteStream `Write` or `BatchUpdateBlobs` requests.

        Blobs that failed to be uploaded will be listed in the response.

        Errors:
        * `INVALID_ARGUMENT`: The client attempted to upload more than the
        server supported limit.

        Individual requests may return the following error, additionally:
        * `NOT_FOUND`: The requested blob is not present in the local cache.
        * `RESOURCE_EXHAUSTED`: There is insufficient disk quota to store the blob.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchTree(self, request, context):
        """Fetch the entire directory tree rooted at a node from a remote CAS to the
        local cache.

        This request is equivalent to `GetTree`, storing the `Directory` objects
        in the local cache. Optionally, this will also fetch all blobs referenced
        by the `Directory` objects, equivalent to `FetchMissingBlobs`.

        If no remote CAS is available, this will check presence of the entire
        directory tree (and optionally also file blobs) in the local cache.

        * `NOT_FOUND`: The requested tree is not present in the CAS or incomplete.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadTree(self, request, context):
        """Upload the entire directory tree from the local cache to a remote CAS.

        This request is equivalent to `UploadMissingBlobs` for all blobs
        referenced by the specified tree (recursively).

        Errors:
        * `NOT_FOUND`: The requested tree root is not present in the local cache.
        * `RESOURCE_EXHAUSTED`: There is insufficient disk quota to store the tree.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StageTree(self, request_iterator, context):
        """Stage a directory tree in the local filesystem.

        This makes the specified directory tree temporarily available for local
        filesystem access. It is implementation-defined whether this uses a
        userspace filesystem such as FUSE, hardlinking or a full copy.

        Missing blobs are fetched, if a CAS remote is configured.

        The staging starts when the server receives the initial request and
        it is ready to be used on the initial (non-error) response from the
        server.

        The server will clean up the staged directory when it either
        receives an additional request (with all fields unset) or when the
        stream is closed. The server will send an additional response after
        cleanup is complete.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CaptureTree(self, request, context):
        """Capture a directory tree from the local filesystem.

        This imports the specified path from the local filesystem into CAS.

        If a CAS remote is configured, the blobs are uploaded.
        The `bypass_local_cache` parameter is a hint to indicate whether the blobs
        shall be uploaded without first storing them in the local cache.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CaptureFiles(self, request, context):
        """Capture files from the local filesystem.

        This imports the specified paths from the local filesystem into CAS.

        If a CAS remote is configured, the blobs are uploaded.
        The `bypass_local_cache` parameter is a hint to indicate whether the blobs
        shall be uploaded without first storing them in the local cache.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstanceNameForRemote(self, request, context):
        """Configure remote CAS endpoint.

        This returns a string that can be used as instance_name to access the
        specified endpoint in further requests.

        DEPRECATED: Use `GetInstanceNameForRemotes()` instead.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetInstanceNameForRemotes(self, request, context):
        """Configure remote endpoints.

        This returns a string that can be used as instance_name to access the
        specified endpoints in further requests.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLocalDiskUsage(self, request, context):
        """Query total space used by the local cache.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LocalContentAddressableStorageServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FetchMissingBlobs': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchMissingBlobs,
                    request_deserializer=build_dot_buildgrid_dot_local__cas__pb2.FetchMissingBlobsRequest.FromString,
                    response_serializer=build_dot_buildgrid_dot_local__cas__pb2.FetchMissingBlobsResponse.SerializeToString,
            ),
            'UploadMissingBlobs': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadMissingBlobs,
                    request_deserializer=build_dot_buildgrid_dot_local__cas__pb2.UploadMissingBlobsRequest.FromString,
                    response_serializer=build_dot_buildgrid_dot_local__cas__pb2.UploadMissingBlobsResponse.SerializeToString,
            ),
            'FetchTree': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchTree,
                    request_deserializer=build_dot_buildgrid_dot_local__cas__pb2.FetchTreeRequest.FromString,
                    response_serializer=build_dot_buildgrid_dot_local__cas__pb2.FetchTreeResponse.SerializeToString,
            ),
            'UploadTree': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadTree,
                    request_deserializer=build_dot_buildgrid_dot_local__cas__pb2.UploadTreeRequest.FromString,
                    response_serializer=build_dot_buildgrid_dot_local__cas__pb2.UploadTreeResponse.SerializeToString,
            ),
            'StageTree': grpc.stream_stream_rpc_method_handler(
                    servicer.StageTree,
                    request_deserializer=build_dot_buildgrid_dot_local__cas__pb2.StageTreeRequest.FromString,
                    response_serializer=build_dot_buildgrid_dot_local__cas__pb2.StageTreeResponse.SerializeToString,
            ),
            'CaptureTree': grpc.unary_unary_rpc_method_handler(
                    servicer.CaptureTree,
                    request_deserializer=build_dot_buildgrid_dot_local__cas__pb2.CaptureTreeRequest.FromString,
                    response_serializer=build_dot_buildgrid_dot_local__cas__pb2.CaptureTreeResponse.SerializeToString,
            ),
            'CaptureFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.CaptureFiles,
                    request_deserializer=build_dot_buildgrid_dot_local__cas__pb2.CaptureFilesRequest.FromString,
                    response_serializer=build_dot_buildgrid_dot_local__cas__pb2.CaptureFilesResponse.SerializeToString,
            ),
            'GetInstanceNameForRemote': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInstanceNameForRemote,
                    request_deserializer=build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemoteRequest.FromString,
                    response_serializer=build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemoteResponse.SerializeToString,
            ),
            'GetInstanceNameForRemotes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInstanceNameForRemotes,
                    request_deserializer=build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemotesRequest.FromString,
                    response_serializer=build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemotesResponse.SerializeToString,
            ),
            'GetLocalDiskUsage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLocalDiskUsage,
                    request_deserializer=build_dot_buildgrid_dot_local__cas__pb2.GetLocalDiskUsageRequest.FromString,
                    response_serializer=build_dot_buildgrid_dot_local__cas__pb2.GetLocalDiskUsageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'build.buildgrid.LocalContentAddressableStorage', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LocalContentAddressableStorage(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def FetchMissingBlobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/build.buildgrid.LocalContentAddressableStorage/FetchMissingBlobs',
            build_dot_buildgrid_dot_local__cas__pb2.FetchMissingBlobsRequest.SerializeToString,
            build_dot_buildgrid_dot_local__cas__pb2.FetchMissingBlobsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadMissingBlobs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/build.buildgrid.LocalContentAddressableStorage/UploadMissingBlobs',
            build_dot_buildgrid_dot_local__cas__pb2.UploadMissingBlobsRequest.SerializeToString,
            build_dot_buildgrid_dot_local__cas__pb2.UploadMissingBlobsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/build.buildgrid.LocalContentAddressableStorage/FetchTree',
            build_dot_buildgrid_dot_local__cas__pb2.FetchTreeRequest.SerializeToString,
            build_dot_buildgrid_dot_local__cas__pb2.FetchTreeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/build.buildgrid.LocalContentAddressableStorage/UploadTree',
            build_dot_buildgrid_dot_local__cas__pb2.UploadTreeRequest.SerializeToString,
            build_dot_buildgrid_dot_local__cas__pb2.UploadTreeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StageTree(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/build.buildgrid.LocalContentAddressableStorage/StageTree',
            build_dot_buildgrid_dot_local__cas__pb2.StageTreeRequest.SerializeToString,
            build_dot_buildgrid_dot_local__cas__pb2.StageTreeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CaptureTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/build.buildgrid.LocalContentAddressableStorage/CaptureTree',
            build_dot_buildgrid_dot_local__cas__pb2.CaptureTreeRequest.SerializeToString,
            build_dot_buildgrid_dot_local__cas__pb2.CaptureTreeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CaptureFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/build.buildgrid.LocalContentAddressableStorage/CaptureFiles',
            build_dot_buildgrid_dot_local__cas__pb2.CaptureFilesRequest.SerializeToString,
            build_dot_buildgrid_dot_local__cas__pb2.CaptureFilesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInstanceNameForRemote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/build.buildgrid.LocalContentAddressableStorage/GetInstanceNameForRemote',
            build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemoteRequest.SerializeToString,
            build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemoteResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetInstanceNameForRemotes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/build.buildgrid.LocalContentAddressableStorage/GetInstanceNameForRemotes',
            build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemotesRequest.SerializeToString,
            build_dot_buildgrid_dot_local__cas__pb2.GetInstanceNameForRemotesResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLocalDiskUsage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/build.buildgrid.LocalContentAddressableStorage/GetLocalDiskUsage',
            build_dot_buildgrid_dot_local__cas__pb2.GetLocalDiskUsageRequest.SerializeToString,
            build_dot_buildgrid_dot_local__cas__pb2.GetLocalDiskUsageResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
