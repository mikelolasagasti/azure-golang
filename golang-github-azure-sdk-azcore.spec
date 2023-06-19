# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/Azure/azure-sdk-for-go
%global goipath         github.com/Azure/azure-sdk-for-go
Version:                1.6.1
%global tag             sdk/azcore/v1.6.1

%gometa -f


%global common_description %{expand:
This repository is for active development of the Azure SDK for Go. For
consumers of the SDK we recommend visiting our public developer docs at:.}

%global golicenses      NOTICE.txt LICENSE.txt sdk/azcore/LICENSE.txt
%global godocs          CODE_OF_CONDUCT.md CONTRIBUTING.md SUPPORT.md\\\
                        SECURITY.md README.md sdk/azcore/CHANGELOG.md \\\
                        sdk/azcore/README.md

Name:           golang-github-azure-sdk-azcore
Release:        %autorelease
Summary:        This repository is for active development of the Azure SDK for Go. For consumers of the SDK we recommend visiting our public developer docs at:

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

rm -rf .github documentation eng profile
pushd sdk
rm -rf azidentity containers data internal keyvault messaging monitor resourcemanager samples security storage template
rm -rf azcore/testdata/
popd

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
