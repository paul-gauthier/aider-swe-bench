NOOP_PATCH = '''diff --git a/empty.file.{nonce}.ignore b/empty.file.{nonce}.ignore
new file mode 100644
index 0000000..e69de29
'''

        "model_patch": NOOP_PATCH.format(nonce="model_patch"), # prediction["model_patch"],
        "test_patch": NOOP_PATCH.format(nonce="test_patch"), # task['test_patch']
    #if iid and prediction['instance_id'] != iid:
    #    continue