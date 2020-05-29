from conans import ConanFile, CMake


class HelloConan(ConanFile):
    name = "hello"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*"
    options = {"zip": [True, False]}
    default_options = {"zip": True}

    def requirements(self):
        if bool(self.options.zip):
            self.requires("zlib/1.2.11")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["WITH_ZIP"] = bool(self.options.zip)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]
