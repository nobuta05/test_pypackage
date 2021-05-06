import setuptools

setuptools.setup(
  name="hello_test",
  version="1.0",
  author="nobuta05",
  author_email="nobuta05@gmail.com",
  description="hello_test is a test package",
  install_requires=["numpy"],
  packages=setuptools.find_packages()
)