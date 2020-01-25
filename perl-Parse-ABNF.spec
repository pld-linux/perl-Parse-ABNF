#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Parse
%define	pnam	ABNF
Summary:	Parse::ABNF - Parse IETF Augmented BNF (ABNF) grammars
Summary(pl.UTF-8):	Parse::ABNF - analizator gramatyk w formacie IETF Augmented BNF (ABNF)
Name:		perl-Parse-ABNF
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Parse/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a2142198e209557850dbbba87253a852
URL:		http://search.cpan.org/dist/Parse-ABNF/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Parse-RecDescent
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses IETF ABNF (STD 68, RFC 5234, 4234, 2234) grammars
into a Perl data structure. It does not generate a parser for the
language described by some ABNF grammar, but makes it easier to turn
an ABNF grammar into a grammar suitable for use with a parser
generator that does not natively support ABNF grammars.

%description -l pl.UTF-8
Ten modu³ analizuje gramatyki w formacie IETF ABNF (STD 68, RFC 5234,
4234, 2234) i przetwarza do postaci struktur danych Perla.
Nie generuje analizatora jêzyka opisanego przez garamtykê, ale u³atwia
zamianê gramatyki ABNF na gramatykê odpowiedni± dla generatorów, które
nie rozumiej± ABNF.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Parse/ABNF.pm
%{_mandir}/man3/*
