#!/usr/bin/env python3
"""Generate a minimal but valid Xcode project for the PhantomClock WatchOS app."""

import os

# Fixed UUIDs (24-char hex, uppercase, Xcode format)
UUID_PROJECT         = "AA000001000000000000001A"
UUID_TARGET          = "AA000001000000000000002A"
UUID_SOURCES_PHASE   = "AA000001000000000000003A"
UUID_FRAMEWORKS_PHASE= "AA000001000000000000004A"
UUID_RESOURCES_PHASE = "AA000001000000000000005A"
UUID_DEBUG_CONFIG    = "AA000001000000000000006A"
UUID_RELEASE_CONFIG  = "AA000001000000000000007A"
UUID_CONFIG_LIST_PROJ= "AA000001000000000000008A"
UUID_CONFIG_LIST_TGT = "AA000001000000000000009A"
UUID_GROUP_MAIN      = "AA000001000000000000010A"
UUID_GROUP_PRODUCTS  = "AA000001000000000000011A"
UUID_PRODUCT_REF     = "AA000001000000000000012A"

UUID_FILE_APP        = "AA000001000000000000020A"
UUID_FILE_CONTENT    = "AA000001000000000000021A"
UUID_FILE_INFO       = "AA000001000000000000022A"

UUID_BUILD_APP       = "AA000001000000000000030A"
UUID_BUILD_CONTENT   = "AA000001000000000000031A"
UUID_BUILD_INFO      = "AA000001000000000000032A"

pbxproj = f"""// !$*UTF8*$!
{{
	archiveVersion = 1;
	classes = {{
	}};
	objectVersion = 56;
	objects = {{

/* Begin PBXBuildFile section */
		{UUID_BUILD_APP} /* PhantomClockApp.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {UUID_FILE_APP} /* PhantomClockApp.swift */; }};
		{UUID_BUILD_CONTENT} /* ContentView.swift in Sources */ = {{isa = PBXBuildFile; fileRef = {UUID_FILE_CONTENT} /* ContentView.swift */; }};
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		{UUID_FILE_APP} /* PhantomClockApp.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = PhantomClockApp.swift; sourceTree = "<group>"; }};
		{UUID_FILE_CONTENT} /* ContentView.swift */ = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ContentView.swift; sourceTree = "<group>"; }};
		{UUID_FILE_INFO} /* Info.plist */ = {{isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; }};
		{UUID_PRODUCT_REF} /* PhantomClock.app */ = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = PhantomClock.app; sourceTree = BUILT_PRODUCTS_DIR; }};
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		{UUID_FRAMEWORKS_PHASE} /* Frameworks */ = {{
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		{UUID_GROUP_PRODUCTS} /* Products */ = {{
			isa = PBXGroup;
			children = (
				{UUID_PRODUCT_REF} /* PhantomClock.app */,
			);
			name = Products;
			sourceTree = "<group>";
		}};
		{UUID_GROUP_MAIN} /* PhantomClock Watch App */ = {{
			isa = PBXGroup;
			children = (
				{UUID_FILE_APP} /* PhantomClockApp.swift */,
				{UUID_FILE_CONTENT} /* ContentView.swift */,
				{UUID_FILE_INFO} /* Info.plist */,
			);
			name = "PhantomClock Watch App";
			path = "PhantomClock Watch App";
			sourceTree = "<group>";
		}};
		{UUID_PROJECT}ROOT /* = */ = {{
			isa = PBXGroup;
			children = (
				{UUID_GROUP_MAIN} /* PhantomClock Watch App */,
				{UUID_GROUP_PRODUCTS} /* Products */,
			);
			sourceTree = "<group>";
		}};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		{UUID_TARGET} /* PhantomClock Watch App */ = {{
			isa = PBXNativeTarget;
			buildConfigurationList = {UUID_CONFIG_LIST_TGT} /* Build configuration list for PBXNativeTarget "PhantomClock Watch App" */;
			buildPhases = (
				{UUID_SOURCES_PHASE} /* Sources */,
				{UUID_FRAMEWORKS_PHASE} /* Frameworks */,
				{UUID_RESOURCES_PHASE} /* Resources */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = "PhantomClock Watch App";
			productName = "PhantomClock Watch App";
			productReference = {UUID_PRODUCT_REF} /* PhantomClock.app */;
			productType = "com.apple.product-type.application";
		}};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		{UUID_PROJECT} /* Project object */ = {{
			isa = PBXProject;
			attributes = {{
				BuildIndependentTargetsInParallel = 1;
				LastSwiftUpdateCheck = 1630;
				LastUpgradeCheck = 1630;
				TargetAttributes = {{
					{UUID_TARGET} = {{
						CreatedOnToolsVersion = 16.3;
					}};
				}};
			}};
			buildConfigurationList = {UUID_CONFIG_LIST_PROJ} /* Build configuration list for PBXProject "PhantomClock" */;
			compatibilityVersion = "Xcode 14.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = {UUID_PROJECT}ROOT;
			productRefGroup = {UUID_GROUP_PRODUCTS} /* Products */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				{UUID_TARGET} /* PhantomClock Watch App */,
			);
		}};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
		{UUID_RESOURCES_PHASE} /* Resources */ = {{
			isa = PBXResourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
		{UUID_SOURCES_PHASE} /* Sources */ = {{
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				{UUID_BUILD_APP} /* PhantomClockApp.swift in Sources */,
				{UUID_BUILD_CONTENT} /* ContentView.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		{UUID_DEBUG_CONFIG}PROJ /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
				CLANG_WARN_BOOL_CONVERSION = YES;
				CLANG_WARN_COMMA = YES;
				CLANG_WARN_CONSTANT_CONVERSION = YES;
				CLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
				CLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
				CLANG_WARN_DOCUMENTATION_COMMENTS = YES;
				CLANG_WARN_EMPTY_BODY = YES;
				CLANG_WARN_ENUM_CONVERSION = YES;
				CLANG_WARN_INFINITE_RECURSION = YES;
				CLANG_WARN_INT_CONVERSION = YES;
				CLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
				CLANG_WARN_OBJC_IMPLICIT_RETAIN_SELF = YES;
				CLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
				CLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
				CLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
				CLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
				CLANG_WARN_STRICT_PROTOTYPES = YES;
				CLANG_WARN_SUSPICIOUS_MOVE = YES;
				CLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
				CLANG_WARN_UNREACHABLE_CODE = YES;
				CLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = YES;
				GCC_C_LANGUAGE_STANDARD = gnu17;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNDECLARED_SELECTOR = YES;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				LOCALIZATION_PREFERS_STRING_CATALOGS = YES;
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = watchos;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = "DEBUG $(inherited)";
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
				WATCHOS_DEPLOYMENT_TARGET = 10.0;
			}};
			name = Debug;
		}};
		{UUID_RELEASE_CONFIG}PROJ /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ALWAYS_SEARCH_USER_PATHS = NO;
				ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS = YES;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_USER_SCRIPT_SANDBOXING = YES;
				GCC_C_LANGUAGE_STANDARD = gnu17;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_WARN_64_TO_32_BIT_CONVERSION = YES;
				GCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
				GCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
				GCC_WARN_UNUSED_FUNCTION = YES;
				GCC_WARN_UNUSED_VARIABLE = YES;
				LOCALIZATION_PREFERS_STRING_CATALOGS = YES;
				MTL_ENABLE_DEBUG_INFO = NO;
				MTL_FAST_MATH = YES;
				SDKROOT = watchos;
				SWIFT_OPTIMIZATION_LEVEL = "-Owholemodule";
				VALIDATE_PRODUCT = YES;
				WATCHOS_DEPLOYMENT_TARGET = 10.0;
			}};
			name = Release;
		}};
		{UUID_DEBUG_CONFIG} /* Debug */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = "PhantomClock Watch App/Info.plist";
				INFOPLIST_KEY_CFBundleDisplayName = "Phantom Clock";
				INFOPLIST_KEY_UISupportedInterfaceOrientations = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown";
				INFOPLIST_KEY_WKApplication = YES;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.boden.phantomclock.watch;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = watchos;
				SKIP_INSTALL = NO;
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = 4;
				WATCHOS_DEPLOYMENT_TARGET = 10.0;
			}};
			name = Debug;
		}};
		{UUID_RELEASE_CONFIG} /* Release */ = {{
			isa = XCBuildConfiguration;
			buildSettings = {{
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Automatic;
				CURRENT_PROJECT_VERSION = 1;
				GENERATE_INFOPLIST_FILE = NO;
				INFOPLIST_FILE = "PhantomClock Watch App/Info.plist";
				INFOPLIST_KEY_CFBundleDisplayName = "Phantom Clock";
				INFOPLIST_KEY_UISupportedInterfaceOrientations = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown";
				INFOPLIST_KEY_WKApplication = YES;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.boden.phantomclock.watch;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SDKROOT = watchos;
				SKIP_INSTALL = NO;
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = 4;
				WATCHOS_DEPLOYMENT_TARGET = 10.0;
			}};
			name = Release;
		}};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		{UUID_CONFIG_LIST_PROJ} /* Build configuration list for PBXProject "PhantomClock" */ = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{UUID_DEBUG_CONFIG}PROJ /* Debug */,
				{UUID_RELEASE_CONFIG}PROJ /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
		{UUID_CONFIG_LIST_TGT} /* Build configuration list for PBXNativeTarget "PhantomClock Watch App" */ = {{
			isa = XCConfigurationList;
			buildConfigurations = (
				{UUID_DEBUG_CONFIG} /* Debug */,
				{UUID_RELEASE_CONFIG} /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		}};
/* End XCConfigurationList section */
	}};
	rootObject = {UUID_PROJECT} /* Project object */;
}}
"""

out_path = os.path.join(os.path.dirname(__file__), "PhantomClock.xcodeproj", "project.pbxproj")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path, "w") as f:
    f.write(pbxproj)

print(f"Written: {out_path}")
