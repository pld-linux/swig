#
# Conditional build:
%bcond_without	guile	# disable guile support
%bcond_without	ocaml	# disable ocaml support
%bcond_without	perl	# disable perl support
%bcond_without	php	# disable php support
%bcond_without	ruby	# disable ruby support
%bcond_without	tcl	# disable tcl support
#
Summary:	Interface generator for Perl, Tcl, Guile and Python
Summary(pl.UTF-8):	Generator interfejsów do Perla, Tcl-a, Guile'a i Pythona
Summary(pt_BR.UTF-8):	Gerador de Interfaces e "Wrappers" Simplificado (SWIG)
Name:		swig
Version:	1.3.35
Release:	1
License:	distributable
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/swig/%{name}-%{version}.tar.gz
# Source0-md5:	9c2ca2332ebcdab55aa98518111d7cc9
Patch0:		%{name}-format.patch
Patch1:		%{name}-php-freearg.patch
Patch2:		%{name}-php-vdecl.patch
URL:		http://www.swig.org/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_guile:BuildRequires:	guile-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
%{?with_ocaml:BuildRequires:	ocaml}
%{?with_perl:BuildRequires:	perl-devel >= 1:5.6.1}
%{?with_php:BuildRequires:	php-cli}
%{?with_php:BuildRequires:	php-devel >= 4.1.0}
BuildRequires:	python-devel >= 1:2.3.2
%if %{with ruby}
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel >= 1:1.6.3
%endif
%{?with_tcl:BuildRequires:	tcl-devel >= 8.3.3}
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

%package guile
Summary:	SWIG library: guile
Summary(pl.UTF-8):	Biblioteka SWIG: guile
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description guile
SWIG library: guile.

%description guile -l pl.UTF-8
Biblioteka SWIG: guile.

%package perl
Summary:	SWIG library: Perl
Summary(pl.UTF-8):	Biblioteka SWIG: Perl
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description perl
SWIG library: perl.

%description perl -l pl.UTF-8
Biblioteka SWIG: perl.

%package php
Summary:	SWIG library: php
Summary(pl.UTF-8):	Biblioteka SWIG: php
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description php
SWIG library: php.

%description php -l pl.UTF-8
Biblioteka SWIG: php.

%package python
Summary:	SWIG library: python
Summary(pl.UTF-8):	Biblioteka SWIG: python
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description python
SWIG library: python.

%description python -l pl.UTF-8
Biblioteka SWIG: python.

%package ruby
Summary:	SWIG library: ruby
Summary(pl.UTF-8):	Biblioteka SWIG: ruby
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%{?ruby_mod_ver_requires_eq}

%description ruby
SWIG library: ruby.

%description ruby -l pl.UTF-8
Biblioteka SWIG: ruby.

%package tcl
Summary:	SWIG library: tcl
Summary(pl.UTF-8):	Biblioteka SWIG: tcl
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tcl
SWIG library: tcl.

%description tcl -l pl.UTF-8
Biblioteka SWIG: tcl.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I Tools/config
%{__autoconf}
%{__automake}
%configure

%{__make} \
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

%files
%defattr(644,root,root,755)
%doc Doc CHANGES CHANGES.current NEW README ANNOUNCE TODO LICENSE
%attr(755,root,root) %{_bindir}/swig
%{_datadir}/%{name}
%{?with_guile:%exclude %{_datadir}/%{name}/%{version}/guile}
%{?with_perl:%exclude %{_datadir}/%{name}/%{version}/perl5}
%{?with_php:%exclude %{_datadir}/%{name}/%{version}/php4}
%exclude %{_datadir}/%{name}/%{version}/python
%{?with_ruby:%exclude %{_datadir}/%{name}/%{version}/ruby}
%{?with_tcl:%exclude %{_datadir}/%{name}/%{version}/tcl}
%{_examplesdir}/%{name}-%{version}

%if %{with guile}
%files guile
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/guile
%endif

%if %{with perl}
%files perl
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/perl5
%endif

%if %{with php}
%files php
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/php4
%endif

%files python
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/python

%if %{with ruby}
%files ruby
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/ruby
%endif

%if %{with tcl}
%files tcl
%defattr(644,root,root,755)
%{_datadir}/%{name}/%{version}/tcl
%endif
