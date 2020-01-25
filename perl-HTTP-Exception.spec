#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	HTTP
%define		pnam	Exception
Summary:	HTTP::Exception - throw HTTP-Errors as (Exception::Class-) Exceptions
Name:		perl-HTTP-Exception
Version:	0.03001
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3541f70932c99c0c44a1d0666bfec151
URL:		http://search.cpan.org/dist/HTTP-Exception/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Exception-Class >= 1.29
BuildRequires:	perl-HTTP-Message >= 5.817
BuildRequires:	perl-Test-Exception >= 0.29
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
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTTP/*.pm
%{perl_vendorlib}/HTTP/Exception
%{_mandir}/man3/*
