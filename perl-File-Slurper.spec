%define	modname	File-Slurper

Summary:	Simple perl module to slurp a file
Name:		perl-%{modname}
Version:	0.014
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		https://metacpan.org/pod/File::Slurper
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/File-Slurper-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warnings)
BuildRequires:	perl-devel
Suggests:	perl(PerlIO::utf8_strict)

%description
Simple perl module to slurp a file

%prep
%autosetup -n %{modname}-%{version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3*/*
