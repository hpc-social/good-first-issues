---
tags: ,priorityP2,statusconfirmed,typebug
title: "Streamlit protobuf names may collide with those of other packages"
html_url: "https://github.com/streamlit/streamlit/issues/3082"
user: thiemoToadi
repo: streamlit/streamlit
---

### Summary

When import streamlit and supervisely_lib together in a project there occurs a TypeError.

### Steps to reproduce

Code snippet:

```
import streamlit as st
import supervisely_lib as sly
```

If applicable, please provide the steps we should take to reproduce the bug:

1. run the code with streamlit run ...
2. see error/traceback when you open the streamlit page


**Expected behavior:**

No error when both libraries are imported together.

**Actual behavior:**

We get the following error/traceback:

`TypeError: Couldn't build proto file into descriptor pool! Invalid proto descriptor for file "worker_api.proto": Empty: "Empty" is already defined in file "streamlit/proto/Empty.proto". Image: "Image" is already defined in file "streamlit/proto/Image.proto". ImagesInfo.infos: "Image" seems to be defined in "streamlit/proto/Image.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. ImagesToAdd.images: "Image" seems to be defined in "streamlit/proto/Image.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. ChunkImage.image: "Image" seems to be defined in "streamlit/proto/Image.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.UploadArchive: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.SetProjectFinished: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.Log: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.GetNewTask: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.GetStopTask: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.AgentPing: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.AgentPing: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.UploadModel: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.GenerateNewModelId: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.GetTelemetryTask: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.UpdateTelemetry: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.UploadImages: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.GetUsedImageList: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.GetUsedModelList: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.GetGeneralEventsStream: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.GetGeneralEventData: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.SendGeneralEventData: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import. GeneralAPI.AddMetaToProject: "Empty" seems to be defined in "streamlit/proto/Empty.proto", which is not imported by "worker_api.proto". To use it here, please add the necessary import.
Traceback:
File "/Users/thiemoseys/PycharmProjects/test_streamlit_with_supervisely/venv/lib/python3.8/site-packages/streamlit/script_runner.py", line 333, in _run_script
    exec(code, module.__dict__)
File "/Users/thiemoseys/PycharmProjects/test_streamlit_with_supervisely/test_imports.py", line 1, in <module>
    import supervisely_lib as sly
File "/Users/thiemoseys/PycharmProjects/test_streamlit_with_supervisely/venv/lib/python3.8/site-packages/supervisely_lib/__init__.py", line 64, in <module>
    import supervisely_lib.worker_proto.worker_api_pb2 as api_proto
File "/Users/thiemoseys/PycharmProjects/test_streamlit_with_supervisely/venv/lib/python3.8/site-packages/supervisely_lib/worker_proto/worker_api_pb2.py", line 18, in <module>
    DESCRIPTOR = _descriptor.FileDescriptor(
File "/Users/thiemoseys/PycharmProjects/test_streamlit_with_supervisely/venv/lib/python3.8/site-packages/google/protobuf/descriptor.py", line 965, in __new__
    return _message.default_pool.AddSerializedFile(serialized_pb)`

### Is this a regression?
i do not know if this has ever worked before.

### Debug info

- Streamlit version: 0.79.0
- Python version: 3.8.3
- Using Conda? VirtualEnvironment 
- OS version: macos Catalina 10.15.5
- Browser version: google chrome 89.0.4389.90 

### Additional information
None