Summary: Interface generator for Perl, Tcl, Guile and Python
Name: swig
Version: 1.1p5
Release: 2
Copyright: distributable
Packager: Oliver Andrich <olli@rhein-zeitung.de>
Group: Development/Languages
Source0: swig1.1p5.tar.gz
Patch: swig1.1p2-fixed-paths.patch
Icon: swig.gif
BuildRoot: /tmp/swig-root

%description
SWIG is a compiler that attempts to make it easy to integrate C, C++,
or Objective-C code with scripting languages including Perl, Tcl, and
Python.  In a nutshell, you give it a bunch of ANSI C/C++ declarations
and it generates an interface between C and your favorite scripting
language.  However, this is only scratching the surface of what SWIG
can do--some of its more advanced features include automatic
documentation generation, module and library management, extensive
customization options, and more.

SWIG is entirely the product of users who have used the system and
suggested new idea.  There are far too many people to thank
individually, but without this support, SWIG would be not be nearly as
powerful or fun to use as it is now. Many thanks!


%prep
%setup -n SWIG1.1p5
find Examples/ -type l -exec rm -v {} \;
%patch -p1

%build
./configure --prefix=/usr
make OPT="$RPM_OPT_FLAGS"
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
make prefix=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc Doc Examples CHANGES Copyright INSTALL NEW README TROUBLESHOOTING ToDo
/usr/lib/swig_lib
/usr/lib/libswig.a
/usr/include/swig.h
/usr/bin/swig
/usr/man/man1/swig.1
