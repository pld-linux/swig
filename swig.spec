Summary: Interface generator for Perl, Tcl, Guile and Python
Summary(pl): Generator interfejsu do Perl'a, Tcl'a, Guile'a i Python'a
Name: swig
Version: 1.1p5
Release: 1
Copyright: distributable
Group: Development/Languages
Group(pl): Programowanie/Jêzyki
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


%description -l pl
SWIG jesk kompilatorem, który próbuje ulatwic integrowanie kodu napisanego
w C, C++ lub Objective-C z jêzykami skryptowymitakimi jak Perl, Tcl i Python.
Mówi±c najpro¶ciej, jesli dostarczysz mu zestaw zdeklarowanych w ANSI C/C++
funkcji, SWIG wygeneruje Ci interfejs pomiedzy C a Twoim ulubionym jêzykiem
skryptowym. To tylko drobna czê¶æ tego co SWIG potrafi robiæ, bardziej 
zaawansowane zastosowania to automatyczne generowanie dokumentacji,
zarzadzanie bibliotekami i modu³ami i wiele innych.

SWIG jest w ca³o¶ci dzi³em ludzi, którzy go u¿ywali i wprowadzali nowe 
pomys³y. Zbyt wielu ich jest, aby dziêkowaæ ka¿demu z nich osobno, 
ale bez ich wsparcia, SWIG nie by³by anie tak pote¿nym na¿edziem, ani tak
fajnym w u¿yciu jak jest teraz. Wiekie dziêki!

%prep
%setup -n SWIG1.1p5
find Examples/ -type l -exec rm -v {} \;
%patch -p1

%build
%configure
make OPT="$RPM_OPT_FLAGS"
make test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
make prefix=$RPM_BUILD_ROOT/usr install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc Examples CHANGES Copyright INSTALL NEW README TROUBLESHOOTING ToDo
%dir %{_libdir}/swig_lib
%{_libdir}/libswig.a
/usr/include/swig.h
%attr(711,root,root) /usr/bin/swig
%{_mandir}/man1/swig.1
