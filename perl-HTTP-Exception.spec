#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	HTTP
%define		pnam	Exception
Summary:	HTTP::Exception - throw HTTP-Errors as (Exception::Class-) Exceptions
Name:		perl-HTTP-Exception
Version:	0.04007
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/T/TM/TMUELLER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c0ad55ba7fb2717c3b93de16522b28d7
URL:		http://search.cpan.org/dist/HTTP-Exception/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Exception-Class >= 1.29
BuildRequires:	perl-HTTP-Message >= 5.817
BuildRequires:	perl-Test-Exception >= 0.29
BuildRequires:	perl-Test-NoWarnings >= 1.04
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Every HTTP::Exception is a Exception::Class - Class. So the same
mechanisms apply as with Exception::Class-classes. In fact have a look
at Exception::Class' docs for more general information on exceptions
and Exception::Class::Base for information on what methods a caught
exception also has.

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
%{perl_vendorlib}/HTTP/*.pm
%{perl_vendorlib}/HTTP/Exception
%{_mandir}/man3/*
