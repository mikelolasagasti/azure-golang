# Generated by go2rpm 1.9.0
# Skip tests as requires internal libraries
# https://stackoverflow.com/posts/59342483/revisions
%bcond_with check
%global debug_package %{nil}

# https://github.com/Azure/azure-sdk-for-go
%global goipath         github.com/Azure/azure-sdk-for-go/sdk/azcore
Version:                1.6.1
%global tag             sdk/azcore/v1.6.1

%gometa -f


%global common_description %{expand:
Azure SDK for Go - azcore library.}

%global golicenses      NOTICE.txt LICENSE.txt sdk/azcore/LICENSE.txt
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md SUPPORT.md\\\
                        SECURITY.md README.md sdk/azcore/CHANGELOG.md \\\
                        sdk/azcore/README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Azure SDK for Go - azcore library

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

# move building library to the root to match goipath
mv sdk/azcore/* .
rm -rf .github documentation eng profile sdk

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
