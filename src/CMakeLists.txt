cmake_minimum_required(VERSION 2.8)
include_directories (${CMAKE_SOURCE_DIR}
                     ${CMAKE_SOURCE_DIR}/src
                     ${CMAKE_SOURCE_DIR}/src/libshared/src
                     ${HOLIDATA_INCLUDE_DIRS})

set (holidata_SRCS holidata.cpp)

set (libshared_SRCS
                    libshared/src/Args.cpp          libshared/src/Args.h
#                    libshared/src/Color.cpp         libshared/src/Color.h
#                    libshared/src/Composite.cpp     libshared/src/Composite.h
#                    libshared/src/Configuration.cpp libshared/src/Configuration.h
#                    libshared/src/Datetime.cpp      libshared/src/Datetime.h
#                    libshared/src/Duration.cpp      libshared/src/Duration.h
#                    libshared/src/FS.cpp            libshared/src/FS.h
#                    libshared/src/JSON.cpp          libshared/src/JSON.h
#                    libshared/src/JSON2.cpp         libshared/src/JSON2.h
#                    libshared/src/Lexer.cpp         libshared/src/Lexer.h
#                    libshared/src/Log.cpp           libshared/src/Log.h
#                    libshared/src/Msg.cpp           libshared/src/Msg.h
#                    libshared/src/Palette.cpp       libshared/src/Palette.h
#                    libshared/src/Pig.cpp           libshared/src/Pig.h
#                    libshared/src/RX.cpp            libshared/src/RX.h
#                    libshared/src/Table.cpp         libshared/src/Table.h
#                    libshared/src/Timer.cpp         libshared/src/Timer.h
#                    libshared/src/Tree.cpp          libshared/src/Tree.h
                    libshared/src/shared.cpp        libshared/src/shared.h
#                    libshared/src/format.cpp        libshared/src/format.h
#                    libshared/src/unicode.cpp       libshared/src/unicode.h
                    libshared/src/utf8.cpp          libshared/src/utf8.h
                    libshared/src/wcwidth6.cpp)

add_library (holidata  STATIC ${holidata_SRCS})
add_library (libshared STATIC ${libshared_SRCS})
add_executable (holidata_executable holidata.cpp)

target_link_libraries (holidata_executable holidata libshared ${HOLIDATA_LIBRARIES})

set_property (TARGET holidata_executable PROPERTY OUTPUT_NAME "holidata")

install (TARGETS holidata_executable DESTINATION bin)

