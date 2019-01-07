from src.converter import Converter

# This is the initial point of execution
if __name__ == '__main__':
    filenames = ["compute", "storage"]
    for f in filenames:
        converter = Converter()
        template = converter.to_jinja(f)
        print(template)

