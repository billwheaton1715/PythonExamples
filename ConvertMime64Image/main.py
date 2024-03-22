import base64
def detect_image_type(image_data):
    # Dictionary of file signatures and corresponding image types
    image_signatures = {
        b'\xFF\xD8': 'jpg',
        b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'png',
        b'\x47\x49\x46\x38\x37': 'gif',
        b'\x47\x49\x46\x38\x39': 'gif',
        b'\x42\x4D': 'bmp'
    }
    
    # Iterate through image signatures and return corresponding image type
    for signature, image_type in image_signatures.items():
        if image_data.startswith(signature):
            return image_type
    
    # If no match is found, return None
    return None

def decode_base64_image_from_xml(xml_file, output_image_file):
    with open(f"C:/Users/bwheaton/code/python_projects/ConvertMime64Image/{xml_file}", 'r') as f:
        xml_content = f.read()

    # Extract the Base64 encoded image data from the XML
    start_index = xml_content.find('<value>') + len('<value>')
    end_index = xml_content.find('</value>')
    base64_data = xml_content[start_index:end_index]

    # Decode the Base64 data
    image_data = base64.b64decode(base64_data)

        # Detect the image type
    image_type = detect_image_type(image_data)
    if image_type:
        print("Detected image type:", image_type)
    else:
        print("Failed to detect image type.")

# Write the decoded data to an image file
    with open(f"C:/Users/bwheaton/code/python_projects/ConvertMime64Image/{output_image_file}.{image_type}", 'wb') as f:
        f.write(image_data)

# Usage example:
decode_base64_image_from_xml('input.xml', 'output')
