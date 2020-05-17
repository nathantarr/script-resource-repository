def run_encrypted_script(script_name, data, ns={}, standalone=True):
    import zlib, base64    
    decoded_data = base64.b64decode(data)
    decompressed_data = zlib.decompress(decoded_data)
    decoded_decompressed_data = decompressed_data.decode()
    corrected_data = decoded_decompressed_data.replace("\r","")
    compiled_data = compile(corrected_data, script_name, 'exec')
    if standalone:
        ns['__name__'] = '__main__'
    exec(compiled_data, ns)

def run_script(script_name, data, ns={}, standalone=True):
    corrected_data = data.replace("\r","")
    compiled_data = compile(corrected_data, script_name, 'exec')
    if standalone:
        ns['__name__'] = '__main__'
    exec(compiled_data, ns)
