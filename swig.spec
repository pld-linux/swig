Summary:	Interface generator for Perl, Tcl, Guile and Python
Summary(pl):	Generator interfejsów do Perla, Tcl-a, Guile'a i Pythona
Summary(pt_BR):	Gerador de Interfaces e "Wrappers" Simplificado (SWIG)
Name:		swig
Version:	1.3.21
Release:	2
License:	distributable
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/swig/%{name}-%{version}.tar.gz
# Source0-md5:	88ff5b99be3eafebb8a6e20f4f986c04
Patch0:		%{name}-format.patch
Patch1:		%{name}-php.patch
Patch2:		%{name}-php-tsrm.patch
Patch3:		%{name}-php-freearg.patch
Patch4:		%{name}-php-vdecl.patch
Patch5:		%{name}-python-lib64.patch
URL:		http://www.swig.org/
Icon:		swig.gif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	guile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ocaml
BuildRequires:	perl-devel >= 1:5.6.1
BuildRequires:	php-devel >= 4.1.0
BuildRequires:	php-cgi
BuildRequires:	python-devel >= 2.3.2
BuildRequires:	ruby >= 1:1.6.3
BuildRequires:	tcl-devel >= 8.3.3
Obsoletes:	swig-ocaml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWIG is a compiler that attempts to make it easy to integrate C, C++,
or Objective-C code with scripting languages including Perl, Tcl, and
Python. In a nutshell, you give it a bunch of ANSI C/C++ declarations
and it generates an interface between C and your favorite scripting
language. However, this is only scratching the surface of what SWIG
can do--some of its more advanced features include automatic
documentation generation, module and library management, extensive
customization options, and more.

SWIG is entirely the product of users who have used the system and
suggested new idea. There are far too many people to thank
individually, but without this support, SWIG would be not be nearly as
powerful or fun to use as it is now. Many thanks!

%description -l pl
SWIG jesk kompilatorem, który próbuje u³atwiæ integrowanie kodu
napisanego w C, C++ lub Objective-C z jêzykami skryptowymi, takimi jak
Perl, Tcl i Python. Mówi±c najpro¶ciej, je¶li dostarczysz mu zestaw
zadeklarowanych w ANSI C/C++ funkcji, SWIG wygeneruje Ci interfejs
pomiêdzy C a Twoim ulubionym jêzykiem skryptowym. To tylko drobna
czê¶æ tego co SWIG potrafi robiæ, bardziej zaawansowane zastosowania
to automatyczne generowanie dokumentacji, zarz±dzanie bibliotekami i
modu³ami i wiele innych.

SWIG jest w ca³o¶ci dzie³em ludzi, którzy go u¿ywali i wprowadzali
nowe pomys³y. Zbyt wielu ich jest, aby dziêkowaæ ka¿demu z nich
osobno, ale bez ich wsparcia SWIG nie by³by ani tak potê¿nym
narzêdziem, ani tak fajnym w u¿yciu jak jest teraz. Wiekie dziêki!

%description -l pt_BR
O SWIG gera interfaces para perl, python e tcl a partir de uma arquivo
com uma interface de descrição que consiste de uma combinação de C/C++
e diretivas especiais. Permite que linguagens tipo script usem C/C++
com um mínimo de esforço.

%package guile
Summary:	SWIG library: guile
Summary(pl):	Biblioteka SWIG: guile
Group:		Libraries

%description guile
SWIG library: guile.

%description guile -l pl
Biblioteka SWIG: guile.

%package perl
Summary:	SWIG library: Perl
Summary(pl):	Biblioteka SWIG: Perl
Group:		Libraries

%description perl
SWIG library: perl.

%description perl -l pl
Biblioteka SWIG: perl.

%package php
Summary:	SWIG library: php
Summary(pl):	Biblioteka SWIG: php
Group:		Libraries

%description php
SWIG library: php.

%description php -l pl
Biblioteka SWIG: php.

%package python
Summary:	SWIG library: python
Summary(pl):	Biblioteka SWIG: python
Group:		Libraries

%description python
SWIG library: python.

%description python -l pl
Biblioteka SWIG: python.

%package ruby
Summary:	SWIG library: ruby
Summary(pl):	Biblioteka SWIG: ruby
Group:		Libraries

%description ruby
SWIG library: ruby.

%description ruby -l pl
Biblioteka SWIG: ruby.

%package tcl
Summary:	SWIG library: tcl
Summary(pl):	Biblioteka SWIG: tcl
Group:		Libraries

%description tcl
SWIG library: tcl.

%description tcl -l pl
Biblioteka SWIG: tcl.

%prep
%setup -q -n SWIG-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%if "%{_lib}" == "lib64"
%patch5 -p1
%endif

%build
%{__libtoolize}
%{__aclocal} -I Tools/config
%{__autoconf}
%configure

%{__make} source runtime \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

%{__make} install install-runtime \
	DESTDIR=$RPM_BUILD_ROOT \
	M4_INSTALL_DIR=$RPM_BUILD_ROOT%{_aclocaldir}

cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	guile -p /sbin/ldconfig
%postun	guile -p /sbin/ldconfig

%post	perl -p /sbin/ldconfig
%postun	perl -p /sbin/ldconfig

%post	php -p /sbin/ldconfig
%postun	php -p /sbin/ldconfig

%post	python -p /sbin/ldconfig
%postun	python -p /sbin/ldconfig

%post	ruby -p /sbin/ldconfig
%postun	ruby -p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Doc CHANGES NEW README ANNOUNCE TODO LICENSE
%{_libdir}/%{name}*
%attr(755,root,root) %{_bindir}/swig
%{_aclocaldir}/swig.m4
%{_examplesdir}/%{name}-%{version}

%files guile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswigguile*.so.*.*.*
%attr(755,root,root) %{_libdir}/libswigguile*.so
%{_libdir}/libswigguile*.la

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswigpl.so.*.*.*
%attr(755,root,root) %{_libdir}/libswigpl.so
%{_libdir}/libswigpl.la

%files php
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswigphp4.so.*.*.*
%attr(755,root,root) %{_libdir}/libswigphp4.so
%{_libdir}/libswigphp4.la

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswigpy.so.*.*.*
%attr(755,root,root) %{_libdir}/libswigpy.so
%{_libdir}/libswigpy.la

%files ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswigrb.so.*.*.*
%attr(755,root,root) %{_libdir}/libswigrb.so
%{_libdir}/libswigrb.la

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libswigtcl*.so.*.*.*
%attr(755,root,root) %{_libdir}/libswigtcl*.so
%{_libdir}/libswigtcl*.la
