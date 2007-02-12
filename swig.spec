Summary:	Interface generator for Perl, Tcl, Guile and Python
Summary(pl.UTF-8):   Generator interfejsów do Perla, Tcl-a, Guile'a i Pythona
Summary(pt_BR.UTF-8):   Gerador de Interfaces e "Wrappers" Simplificado (SWIG)
Name:		swig
Version:	1.3.24
Release:	1
License:	distributable
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/swig/%{name}-%{version}.tar.gz
# Source0-md5:	c5fc655dbbb6fe0cfab2211747dadbe0
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
BuildRequires:	python-devel >= 1:2.3.2
BuildRequires:	ruby >= 1:1.6.3
BuildRequires:	tcl-devel >= 8.3.3
Obsoletes:	swig-guile
Obsoletes:	swig-ocaml
Obsoletes:	swig-perl
Obsoletes:	swig-php
Obsoletes:	swig-python
Obsoletes:	swig-ruby
Obsoletes:	swig-tcl
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

%description -l pl.UTF-8
SWIG jesk kompilatorem, który próbuje ułatwić integrowanie kodu
napisanego w C, C++ lub Objective-C z językami skryptowymi, takimi jak
Perl, Tcl i Python. Mówiąc najprościej, jeśli dostarczysz mu zestaw
zadeklarowanych w ANSI C/C++ funkcji, SWIG wygeneruje Ci interfejs
pomiędzy C a Twoim ulubionym językiem skryptowym. To tylko drobna
część tego co SWIG potrafi robić, bardziej zaawansowane zastosowania
to automatyczne generowanie dokumentacji, zarządzanie bibliotekami i
modułami i wiele innych.

SWIG jest w całości dziełem ludzi, którzy go używali i wprowadzali
nowe pomysły. Zbyt wielu ich jest, aby dziękować każdemu z nich
osobno, ale bez ich wsparcia SWIG nie byłby ani tak potężnym
narzędziem, ani tak fajnym w użyciu jak jest teraz. Wiekie dzięki!

%description -l pt_BR.UTF-8
O SWIG gera interfaces para perl, python e Tcl a partir de uma arquivo
com uma interface de descrição que consiste de uma combinação de C/C++
e diretivas especiais. Permite que linguagens tipo script usem C/C++
com um mínimo de esforço.

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
%{__autoheader}
%{__automake}
%configure

%{__make} source \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	M4_INSTALL_DIR=$RPM_BUILD_ROOT%{_aclocaldir}

cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES* FUTURE LICENSE NEW README TODO Doc
%attr(755,root,root) %{_bindir}/swig
%{_datadir}/swig
%{_examplesdir}/%{name}-%{version}
