user_data = """
    #!/bin/bash
    echo "Hello, world!" > index.html
    nohup python -m SimpleHTTPServer 80 &
    """
