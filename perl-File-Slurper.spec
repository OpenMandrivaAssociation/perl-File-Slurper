%define	modname	File-Slurper
%define	modver	0.013

Summary:	Simple perl module to slurp a file
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
Group:		Development/Perl
License:	GPLv2+ or Artistic
Url:		http://metacpan.org/pod/File::Slurper
Source0:	http://search.cpan.org/CPAN/authors/id/L/LE/LEONT/File-Slurper-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warnings)
BuildRequires:	perl-devel
Suggests:	perl(PerlIO::utf8_strict)

%description
Simple perl module to slurp a file

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%make_install

%files
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3*/*
