Name: zola
Version: 0.5.0
Release: 1%{?dist}
Summary: A search tool that combines the usability of ag with the raw speed of grep
License: MIT or Unlicense
URL: https://github.com/getzola/zola
Source0: https://github.com/getzola/zola/archive/%{version}/zola-%{version}.tar.gz
BuildRequires: cargo
BuildRequires: asciidoc
%if 0%{?fedora} >= 24
ExclusiveArch: x86_64 i686 armv7hl
%else
ExclusiveArch: x86_64 aarch64
%endif


%description
A fast static site generator in a single binary with everything built-in.


%prep
%autosetup


%build
cargo build --release


%install
install -D -p -m 755 target/release/zola %{buildroot}%{_bindir}/zola


%check
cargo test


%files
%license COPYING LICENSE-MIT UNLICENSE
%doc README.md CHANGELOG.md GUIDE.md FAQ.md
%{_bindir}/rg
%{_mandir}/man1/rg.1*
%{_datadir}/bash-completion
%{_datadir}/fish
%{_datadir}/zsh


%changelog
* Mon Nov 19 2018 Baptiste Darthenay <baptiste.darthenay@gmail.com> - 0.5.0-1
- Initial spec file
