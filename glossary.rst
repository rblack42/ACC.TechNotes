..  _glossary:

########
Glossary
########

..  include::   /references.inc

..  glossary::
    :sorted:

    Integrated Development Environment
    IDE
        A program that manages programming projects. Typically, this tool runs
        a variety of standard programming tools, including editors, compilers,
        and debuggers, to help make programmers more productive.

    sketch
        A simplified C/C++ program designed to be run on an Arduino_ processor.
        The code is not complete, and the missing parts are proviced by the
        Arduino_ :term:`IDE`.

    Cloud
        A term that refers to the INternet, but specifically to servers hosting
        services we use on the Internet. Many folks depend on servers run bu
        companies like RackSpace_ and do not own and operate their own
        equipment!

    object file
    object files
        Compilers translate a :term:`source file` into someting closer to
        :term:`machine language` for the target computer. This file has holes
        where the :term:`source file` referred to something not located in this
        particular file

    source file
    source files
        A text file containing a program written in some programming language.

    include file
    include files 
        A file designed to be "included" in another file by the program
        processing that second file. Typically, a compiler reads an
        :term:`include file` that contains information about program components
        that are available to the program from one of more system
        :term:`library` files.

    hex file
        Many microcontroller systems use a simple text file to hold the code
        for that processor. This code is in the fown of a series of hexadecimal
        characters representing the binary data to be sent to the processor by
        a loader program. Intel developed this format back in the 1970s when
        microprocessors were very new!

    library
        A single file containing a set of other files. Typically, programmers
        use libraries to hold a set of :term:`object files` that the linker can
        search through as it looks for missing components of a program.

    path
    system path
        A string indicating where a file is located on the system. Typically,
        files are envisioned as being located in directories and
        subdirectoruies, or folders and sub-folders on a PC. The idea is that
        we have folders inside other folders where a file is stored. The
        :term:`path` tells humans where the file is located. Each component of
        the :term:`path` is separated by either a forward slash (on Linux/Mac)
        or a backward slash (Windows). Each time we move past a slash, we have
        moved down into a contained sub-folder. When the :term:`path` starts at
        the top of the system (a drive on a PC, or the top of the directory
        "tree" on linux/Mac), we start the payh with a single slash. PC users
        add a drive letter in front of this

    machine language
    machine code
        The actual binary codes understood by the processor in a particular
        computer. These codes were designed by the manufacturer of that
        processor. A compiler needs to be able to generate these codes from a
        program if that program is to run on that particular processor.

    executable
    executable file
        A file containing the :term:`machine code` needed by a particular
        computer. This file is not pure :term:`machine language`. Instead is is
        a data file read by some loader program that lays the contents into the
        memory of the computer so the program can be run. Typically this loader
        is something the operating system runs when you command that a program
        be run on that system

    VM
    Virtual Machine
        A program that emulates a real computer accurately enough to run real
        programs for that computer.

    command line
    command prompt
        The place where you type commands to control your computer. Usually
        done in a :program:`cmd` window on PCs, or in a
        :program:`Terminal` program on Mac/Linux.

    VPS
    Virtual Private Server 
        A server provided by a company like Rackspace.  Usually this is a
        :term:`VM` running on a real server somewhere on the :term:`Cloud`.
