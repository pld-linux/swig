
Summary:	Interface generator for Perl, Tcl, Guile and Python
Summary(pl):	Generator interfejs�w do Perla, Tcl-a, Guile'a i Pythona
Summary(pt_BR):	Gerador de Interfaces e "Wrappers" Simplificado (SWIG)
Name:		swig
Version:	1.3.19
Release:	7
License:	distributable
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/swig/%{name}-%{version}.tar.gz
# Source0-md5:	a733455544426b31868dd87fc162e750
Patch0:		%{name}-format.patch
Patch1:		%{name}-php.patch
Patch2:		%{name}-php-tsrm.patch
Patch3:		%{name}-php-freearg.patch
Patch4:		%{name}-php-vdecl.patch
URL:		http://www.swig.org/
Icon:		swig.gif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	guile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	php-devel >= 4.1.0
BuildRequires:	php-cgi
BuildRequires:	python-devel >= 2.3.2
BuildRequires:	ruby >= 1.6.3
BuildRequires:	tcl-devel >= 8.3.3
BuildRequires:	ocaml
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
SWIG jesk kompilatorem, kt�ry pr�buje u�atwi� integrowanie kodu
napisanego w C, C++ lub Objective-C z j�zykami skryptowymi, takimi jak
Perl, Tcl i Python. M�wi�c najpro�ciej, je�li dostarczysz mu zestaw
zadeklarowanych w ANSI C/C++ funkcji, SWIG wygeneruje Ci interfejs
pomi�dzy C a Twoim ulubionym j�zykiem skryptowym. To tylko drobna
cz�� tego co SWIG potrafi robi�, bardziej zaawansowane zastosowania
to automatyczne generowanie dokumentacji, zarz�dzanie bibliotekami i
modu�ami i wiele innych.

SWIG jest w ca�o�ci dzie�em ludzi, kt�rzy go u�ywali i wprowadzali
nowe pomys�y. Zbyt wielu ich jest, aby dzi�kowa� ka�demu z nich
osobno, ale bez ich wsparcia SWIG nie by�by ani tak pot�nym
narz�dziem, ani tak fajnym w u�yciu jak jest teraz. Wiekie dzi�ki!

%description -l pt_BR
O SWIG gera interfaces para perl, python e tcl a partir de uma arquivo
com uma interface de descri��o que consiste de uma combina��o de C/C++
e diretivas especiais. Permite que linguagens tipo script usem C/C++
com um m�nimo de esfor�o.

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

%package ocaml
Summary:	SWIG library: ocaml
Summary(pl):	Biblioteka SWIG: ocaml
Group:		Libraries

%description ocaml
SWIG library: ocaml.

%description ocaml -l pl
Biblioteka SWIG: ocaml.

%prep
%setup -q -n SWIG-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
oldpwd=$PWD
for i in . Tools; do
  cd $i
  %{__libtoolize}
  %{__aclocal}
  %{__autoconf}
  cd $oldpwd
done
%configure

%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Doc CHANGES NEW README ANNOUNCE TODO LICENSE
%{_libdir}/%{name}*
%attr(755,root,root) %{_bindir}/swig
%{_examplesdir}/%{name}-%{version}

%files guile
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*guile.so
%{_libdir}/lib*guile.la

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*pl.so
%{_libdir}/lib*pl.la

%files php
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*php4.so
%{_libdir}/lib*php4.la

%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*py.so
%{_libdir}/lib*py.la

%files ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*rb.so
%{_libdir}/lib*rb.la

%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*tcl*.so
%{_libdir}/lib*tcl*.la

%files ocaml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*ocaml*.so*
%{_libdir}/lib*ocaml*.la
