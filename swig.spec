Summary:	Interface generator for Perl, Tcl, Guile and Python
Summary(pl):	Generator interfejsu do Perl'a, Tcl'a, Guile'a i Python'a
Name:		swig
Version:	1.3.11
Release:	1
License:	distributable
Group:		Development/Languages
Source0:	http://prdownloads.sourceforge.net/swig/%{name}-%{version}.tar.gz
Patch0:		%{name}-configure.patch
URL:		http://www.swig.org
BuildRequires:	autoconf
BuildRequires:	guile-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	php-devel >= 4.1.0
BuildRequires:	python >= 2.2
BuildRequires:	ruby >= 1.6.3
BuildRequires:	tcl >= 8.3.3
Icon:		swig.gif
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
SWIG jesk kompilatorem, który próbuje ulatwic integrowanie kodu
napisanego w C, C++ lub Objective-C z jêzykami skryptowymitakimi jak
Perl, Tcl i Python. Mówi±c najpro¶ciej, jesli dostarczysz mu zestaw
zdeklarowanych w ANSI C/C++ funkcji, SWIG wygeneruje Ci interfejs
pomiedzy C a Twoim ulubionym jêzykiem skryptowym. To tylko drobna
czê¶æ tego co SWIG potrafi robiæ, bardziej zaawansowane zastosowania
to automatyczne generowanie dokumentacji, zarzadzanie bibliotekami i
modu³ami i wiele innych.

SWIG jest w ca³o¶ci dzi³em ludzi, którzy go u¿ywali i wprowadzali nowe
pomys³y. Zbyt wielu ich jest, aby dziêkowaæ ka¿demu z nich osobno, ale
bez ich wsparcia, SWIG nie by³by anie tak pote¿nym na¿edziem, ani tak
fajnym w u¿yciu jak jest teraz. Wiekie dziêki!

%prep
%setup -q -n SWIG-%{version}
%patch0 -p1

%build
oldpwd=$PWD
for i in . Source/DOH Tools Examples/GIFPlot; do
  cd $i
  aclocal
  autoconf
  cd $oldpwd
done
%configure
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a Examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf CHANGES NEW README ANNOUNCE TODO LICENSE

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Doc *.gz
%{_libdir}/%{name}*
%attr(755,root,root) %{_bindir}/swig
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_examplesdir}/%{name}-%{version}
