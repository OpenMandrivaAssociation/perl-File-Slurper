%define	modname	File-Slurper
%define	modver	0.012

Summary:	Simple perl module to slurp a file
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/File-Slurper-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
Suggests:	perl(PerlIO::utf8_strict)

%description
Simple perl module to slurp a file

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3*/*
