Name:           ffmpeg
Version:        3.0.4
Release:        1%{?dist}
Summary:        A complete, cross-platform solution to record, convert and stream audio and video. 

License:        LGPL 2.1
URL:            https://ffmpeg.org/
Source0:        http://ffmpeg.org/releases/ffmpeg-%{version}.tar.bz2

BuildRequires:  SDL-devel 
Requires:       SDL

%description
FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge. No matter if they were designed by some standards committee, the community or a corporation.

%prep
%setup -q


%build
./configure \
    --enable-ffplay
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%doc



%changelog
* Sun Jun 19 2016 Tadeáš Ursíny <thatisgeek@gmail.com> 3.0.4-1
- new package built with tito

* Sun Jun 19 2016 Tadeáš Ursíny <thatisgeek@gmail.com> 3.0.3-1
- new package built with tito

* Sun May 15 2016 Tadeáš Ursíny
- 
