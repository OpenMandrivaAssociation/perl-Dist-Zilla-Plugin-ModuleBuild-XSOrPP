%define upstream_name    Dist-Zilla-Plugin-ModuleBuild-XSOrPP
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Add a --pp option to your Build.PL to force an XS-less build
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://git.urth.org/Dist-Zilla-Plugin-ModuleBuild-XSOrPP
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Dist-Zilla-Plugin-ModuleBuild-XSOrPP-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Most)
BuildArch:	noarch

%description
Use this plugin instead of the regular 'ModuleBuild' plugin. It generates a
_Build.PL_ which accepts a '--pp' flag to forcible disable XS compilation.
Obviously, this is only useful if your module can work without its XS
component.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

