Name:           vk-hdr-layer-gnome47
Version:        main
Release:        %autorelease
Summary:     Vulkan layer for HDR on Gnome 47

License:        MIT
URL:            https://github.com/swick/VK_hdr_layer
Source:         https://github.com/swick/VK_hdr_layer/archive/refs/heads/main.tar.gz

BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(vkroots)

%description
Simple package of Swick's VK_hdr_layer, used for experimental HDR on Gnome 47.

Probably broken, just experimenting at the moment

%prep
%setup -n VK_hdr_layer-%version

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_datadir}/vulkan/implicit_layer.d/*
%{_libdir}/*.so
