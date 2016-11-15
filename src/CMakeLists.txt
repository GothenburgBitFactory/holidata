cmake_minimum_required(VERSION 2.8)
include_directories (${CMAKE_SOURCE_DIR}
                     ${CMAKE_SOURCE_DIR}/src
                     ${CMAKE_SOURCE_DIR}/src/libshared/src
                     ${HOLIDATA_INCLUDE_DIRS})

set (holidata_SRCS holidata.cpp)

set (libshared_SRCS libshared/src/Args.cpp libshared/src/Args.h)

add_library (holidata  STATIC ${holidata_SRCS})
add_library (libshared STATIC ${libshared_SRCS})
add_executable (holidata_executable holidata.cpp)

target_link_libraries (holidata_executable holidata libshared ${HOLIDATA_LIBRARIES})

set_property (TARGET holidata_executable PROPERTY OUTPUT_NAME "holidata")

install (TARGETS holidata_executable DESTINATION bin)

