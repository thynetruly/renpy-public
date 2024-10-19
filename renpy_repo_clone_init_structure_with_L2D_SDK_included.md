```plaintext
renpy
├── .git (contents omitted for brevity)
├── .vscode
│  ├── settings.json
│  └── tasks.json
├── CubismSdkForNative-5-r.1
│  ├── Core
│  │  ├── dll
│  │  │  ├── android
│  │  │  │  ├── arm64-v8a
│  │  │  │  │  └── libLive2DCubismCore.so
│  │  │  │  ├── armeabi-v7a
│  │  │  │  │  └── libLive2DCubismCore.so
│  │  │  │  ├── x86
│  │  │  │  │  └── libLive2DCubismCore.so
│  │  │  │  └── x86_64
│  │  │  │     └── libLive2DCubismCore.so
│  │  │  ├── experimental
│  │  │  │  ├── rpi
│  │  │  │  │  └── libLive2DCubismCore.so
│  │  │  │  └── uwp
│  │  │  │     ├── arm
│  │  │  │     │  └── Live2DCubismCore.dll
│  │  │  │     ├── arm64
│  │  │  │     │  └── Live2DCubismCore.dll
│  │  │  │     ├── x64
│  │  │  │     │  └── Live2DCubismCore.dll
│  │  │  │     └── x86
│  │  │  │        └── Live2DCubismCore.dll
│  │  │  ├── linux
│  │  │  │  └── x86_64
│  │  │  │     └── libLive2DCubismCore.so
│  │  │  ├── macos
│  │  │  │  ├── libLive2DCubismCore.dylib
│  │  │  │  └── Live2DCubismCore.bundle
│  │  │  └── windows
│  │  │     ├── x86
│  │  │     │  ├── Live2DCubismCore.dll
│  │  │     │  └── Live2DCubismCore.lib
│  │  │     └── x86_64
│  │  │        ├── Live2DCubismCore.dll
│  │  │        └── Live2DCubismCore.lib
│  │  ├── include
│  │  │  └── Live2DCubismCore.h
│  │  ├── lib
│  │  │  ├── android
│  │  │  │  ├── arm64-v8a
│  │  │  │  │  └── libLive2DCubismCore.a
│  │  │  │  ├── armeabi-v7a
│  │  │  │  │  └── libLive2DCubismCore.a
│  │  │  │  ├── x86
│  │  │  │  │  └── libLive2DCubismCore.a
│  │  │  │  └── x86_64
│  │  │  │     └── libLive2DCubismCore.a
│  │  │  ├── experimental
│  │  │  │  ├── catalyst
│  │  │  │  │  └── libLive2DCubismCore.a
│  │  │  │  └── rpi
│  │  │  │     └── libLive2DCubismCore.a
│  │  │  ├── ios
│  │  │  │  ├── Debug-iphoneos
│  │  │  │  │  └── libLive2DCubismCore.a
│  │  │  │  ├── Debug-iphonesimulator
│  │  │  │  │  └── libLive2DCubismCore.a
│  │  │  │  ├── Release-iphoneos
│  │  │  │  │  └── libLive2DCubismCore.a
│  │  │  │  └── Release-iphonesimulator
│  │  │  │     └── libLive2DCubismCore.a
│  │  │  ├── linux
│  │  │  │  └── x86_64
│  │  │  │     └── libLive2DCubismCore.a
│  │  │  ├── macos
│  │  │  │  ├── arm64
│  │  │  │  │  └── libLive2DCubismCore.a
│  │  │  │  └── x86_64
│  │  │  │     └── libLive2DCubismCore.a
│  │  │  └── windows
│  │  │     ├── x86
│  │  │     │  ├── 120
│  │  │     │  │  ├── Live2DCubismCore_MD.lib
│  │  │     │  │  ├── Live2DCubismCore_MDd.lib
│  │  │     │  │  ├── Live2DCubismCore_MT.lib
│  │  │     │  │  └── Live2DCubismCore_MTd.lib
│  │  │     │  ├── 140
│  │  │     │  │  ├── Live2DCubismCore_MD.lib
│  │  │     │  │  ├── Live2DCubismCore_MDd.lib
│  │  │     │  │  ├── Live2DCubismCore_MT.lib
│  │  │     │  │  └── Live2DCubismCore_MTd.lib
│  │  │     │  ├── 141
│  │  │     │  │  ├── Live2DCubismCore_MD.lib
│  │  │     │  │  ├── Live2DCubismCore_MDd.lib
│  │  │     │  │  ├── Live2DCubismCore_MT.lib
│  │  │     │  │  └── Live2DCubismCore_MTd.lib
│  │  │     │  ├── 142
│  │  │     │  │  ├── Live2DCubismCore_MD.lib
│  │  │     │  │  ├── Live2DCubismCore_MDd.lib
│  │  │     │  │  ├── Live2DCubismCore_MT.lib
│  │  │     │  │  └── Live2DCubismCore_MTd.lib
│  │  │     │  └── 143
│  │  │     │     ├── Live2DCubismCore_MD.lib
│  │  │     │     ├── Live2DCubismCore_MDd.lib
│  │  │     │     ├── Live2DCubismCore_MT.lib
│  │  │     │     └── Live2DCubismCore_MTd.lib
│  │  │     └── x86_64
│  │  │        ├── 120
│  │  │        │  ├── Live2DCubismCore_MD.lib
│  │  │        │  ├── Live2DCubismCore_MDd.lib
│  │  │        │  ├── Live2DCubismCore_MT.lib
│  │  │        │  └── Live2DCubismCore_MTd.lib
│  │  │        ├── 140
│  │  │        │  ├── Live2DCubismCore_MD.lib
│  │  │        │  ├── Live2DCubismCore_MDd.lib
│  │  │        │  ├── Live2DCubismCore_MT.lib
│  │  │        │  └── Live2DCubismCore_MTd.lib
│  │  │        ├── 141
│  │  │        │  ├── Live2DCubismCore_MD.lib
│  │  │        │  ├── Live2DCubismCore_MDd.lib
│  │  │        │  ├── Live2DCubismCore_MT.lib
│  │  │        │  └── Live2DCubismCore_MTd.lib
│  │  │        ├── 142
│  │  │        │  ├── Live2DCubismCore_MD.lib
│  │  │        │  ├── Live2DCubismCore_MDd.lib
│  │  │        │  ├── Live2DCubismCore_MT.lib
│  │  │        │  └── Live2DCubismCore_MTd.lib
│  │  │        └── 143
│  │  │           ├── Live2DCubismCore_MD.lib
│  │  │           ├── Live2DCubismCore_MDd.lib
│  │  │           ├── Live2DCubismCore_MT.lib
│  │  │           └── Live2DCubismCore_MTd.lib
│  │  ├── CHANGELOG.md
│  │  ├── LICENSE.md
│  │  ├── README.ja.md
│  │  ├── README.md
│  │  └── RedistributableFiles.txt
│  ├── Framework
│  │  ├── src
│  │  │  ├── Effect
│  │  │  │  ├── CMakeLists.txt
│  │  │  │  ├── CubismBreath.cpp
│  │  │  │  ├── CubismBreath.hpp
│  │  │  │  ├── CubismEyeBlink.cpp
│  │  │  │  ├── CubismEyeBlink.hpp
│  │  │  │  ├── CubismPose.cpp
│  │  │  │  └── CubismPose.hpp
│  │  │  ├── Id
│  │  │  │  ├── CMakeLists.txt
│  │  │  │  ├── CubismId.cpp
│  │  │  │  ├── CubismId.hpp
│  │  │  │  ├── CubismIdManager.cpp
│  │  │  │  └── CubismIdManager.hpp
│  │  │  ├── Math
│  │  │  │  ├── CMakeLists.txt
│  │  │  │  ├── CubismMath.cpp
│  │  │  │  ├── CubismMath.hpp
│  │  │  │  ├── CubismMatrix44.cpp
│  │  │  │  ├── CubismMatrix44.hpp
│  │  │  │  ├── CubismModelMatrix.cpp
│  │  │  │  ├── CubismModelMatrix.hpp
│  │  │  │  ├── CubismTargetPoint.cpp
│  │  │  │  ├── CubismTargetPoint.hpp
│  │  │  │  ├── CubismVector2.cpp
│  │  │  │  ├── CubismVector2.hpp
│  │  │  │  ├── CubismViewMatrix.cpp
│  │  │  │  └── CubismViewMatrix.hpp
│  │  │  ├── Model
│  │  │  │  ├── CMakeLists.txt
│  │  │  │  ├── CubismMoc.cpp
│  │  │  │  ├── CubismMoc.hpp
│  │  │  │  ├── CubismModel.cpp
│  │  │  │  ├── CubismModel.hpp
│  │  │  │  ├── CubismModelUserData.cpp
│  │  │  │  ├── CubismModelUserData.hpp
│  │  │  │  ├── CubismModelUserDataJson.cpp
│  │  │  │  ├── CubismModelUserDataJson.hpp
│  │  │  │  ├── CubismUserModel.cpp
│  │  │  │  └── CubismUserModel.hpp
│  │  │  ├── Motion
│  │  │  │  ├── ACubismMotion.cpp
│  │  │  │  ├── ACubismMotion.hpp
│  │  │  │  ├── CMakeLists.txt
│  │  │  │  ├── CubismExpressionMotion.cpp
│  │  │  │  ├── CubismExpressionMotion.hpp
│  │  │  │  ├── CubismExpressionMotionManager.cpp
│  │  │  │  ├── CubismExpressionMotionManager.hpp
│  │  │  │  ├── CubismMotion.cpp
│  │  │  │  ├── CubismMotion.hpp
│  │  │  │  ├── CubismMotionInternal.hpp
│  │  │  │  ├── CubismMotionJson.cpp
│  │  │  │  ├── CubismMotionJson.hpp
│  │  │  │  ├── CubismMotionManager.cpp
│  │  │  │  ├── CubismMotionManager.hpp
│  │  │  │  ├── CubismMotionQueueEntry.cpp
│  │  │  │  ├── CubismMotionQueueEntry.hpp
│  │  │  │  ├── CubismMotionQueueManager.cpp
│  │  │  │  └── CubismMotionQueueManager.hpp
│  │  │  ├── Physics
│  │  │  │  ├── CMakeLists.txt
│  │  │  │  ├── CubismPhysics.cpp
│  │  │  │  ├── CubismPhysics.hpp
│  │  │  │  ├── CubismPhysicsInternal.hpp
│  │  │  │  ├── CubismPhysicsJson.cpp
│  │  │  │  └── CubismPhysicsJson.hpp
│  │  │  ├── Rendering
│  │  │  │  ├── Cocos2d
│  │  │  │  │  ├── CMakeLists.txt
│  │  │  │  │  ├── CubismCommandBuffer_Cocos2dx.cpp
│  │  │  │  │  ├── CubismCommandBuffer_Cocos2dx.hpp
│  │  │  │  │  ├── CubismOffscreenSurface_Cocos2dx.cpp
│  │  │  │  │  ├── CubismOffscreenSurface_Cocos2dx.hpp
│  │  │  │  │  ├── CubismRenderer_Cocos2dx.cpp
│  │  │  │  │  ├── CubismRenderer_Cocos2dx.hpp
│  │  │  │  │  ├── CubismShader_Cocos2dx.cpp
│  │  │  │  │  └── CubismShader_Cocos2dx.hpp
│  │  │  │  ├── D3D11
│  │  │  │  │  ├── CMakeLists.txt
│  │  │  │  │  ├── CubismNativeInclude_D3D11.hpp
│  │  │  │  │  ├── CubismOffscreenSurface_D3D11.cpp
│  │  │  │  │  ├── CubismOffscreenSurface_D3D11.hpp
│  │  │  │  │  ├── CubismRenderer_D3D11.cpp
│  │  │  │  │  ├── CubismRenderer_D3D11.hpp
│  │  │  │  │  ├── CubismRenderState_D3D11.cpp
│  │  │  │  │  ├── CubismRenderState_D3D11.hpp
│  │  │  │  │  ├── CubismShader_D3D11.cpp
│  │  │  │  │  ├── CubismShader_D3D11.hpp
│  │  │  │  │  └── CubismType_D3D11.hpp
│  │  │  │  ├── D3D9
│  │  │  │  │  ├── CMakeLists.txt
│  │  │  │  │  ├── CubismNativeInclude_D3D9.hpp
│  │  │  │  │  ├── CubismOffscreenSurface_D3D9.cpp
│  │  │  │  │  ├── CubismOffscreenSurface_D3D9.hpp
│  │  │  │  │  ├── CubismRenderer_D3D9.cpp
│  │  │  │  │  ├── CubismRenderer_D3D9.hpp
│  │  │  │  │  ├── CubismRenderState_D3D9.cpp
│  │  │  │  │  ├── CubismRenderState_D3D9.hpp
│  │  │  │  │  ├── CubismShader_D3D9.cpp
│  │  │  │  │  ├── CubismShader_D3D9.hpp
│  │  │  │  │  └── CubismType_D3D9.hpp
│  │  │  │  ├── Metal
│  │  │  │  │  ├── CMakeLists.txt
│  │  │  │  │  ├── CubismCommandBuffer_Metal.hpp
│  │  │  │  │  ├── CubismCommandBuffer_Metal.mm
│  │  │  │  │  ├── CubismOffscreenSurface_Metal.hpp
│  │  │  │  │  ├── CubismOffscreenSurface_Metal.mm
│  │  │  │  │  ├── CubismRenderer_Metal.hpp
│  │  │  │  │  ├── CubismRenderer_Metal.mm
│  │  │  │  │  ├── CubismRenderingInstanceSingleton_Metal.h
│  │  │  │  │  ├── CubismRenderingInstanceSingleton_Metal.m
│  │  │  │  │  ├── CubismShader_Metal.hpp
│  │  │  │  │  ├── CubismShader_Metal.mm
│  │  │  │  │  ├── MetalShaders.metal
│  │  │  │  │  └── MetalShaderTypes.h
│  │  │  │  ├── OpenGL
│  │  │  │  │  ├── CMakeLists.txt
│  │  │  │  │  ├── CubismOffscreenSurface_OpenGLES2.cpp
│  │  │  │  │  ├── CubismOffscreenSurface_OpenGLES2.hpp
│  │  │  │  │  ├── CubismRenderer_OpenGLES2.cpp
│  │  │  │  │  ├── CubismRenderer_OpenGLES2.hpp
│  │  │  │  │  ├── CubismShader_OpenGLES2.cpp
│  │  │  │  │  └── CubismShader_OpenGLES2.hpp
│  │  │  │  ├── Vulkan
│  │  │  │  │  ├── Shaders
│  │  │  │  │  │  ├── src
│  │  │  │  │  │  │  ├── common.glsl
│  │  │  │  │  │  │  ├── FragShaderSrc.frag
│  │  │  │  │  │  │  ├── FragShaderSrcMask.frag
│  │  │  │  │  │  │  ├── FragShaderSrcMaskInverted.frag
│  │  │  │  │  │  │  ├── FragShaderSrcMaskInvertedPremultipliedAlpha.frag
│  │  │  │  │  │  │  ├── FragShaderSrcMaskPremultipliedAlpha.frag
│  │  │  │  │  │  │  ├── FragShaderSrcPremultipliedAlpha.frag
│  │  │  │  │  │  │  ├── FragShaderSrcSetupMask.frag
│  │  │  │  │  │  │  ├── VertShaderSrc.vert
│  │  │  │  │  │  │  ├── VertShaderSrcMasked.vert
│  │  │  │  │  │  │  └── VertShaderSrcSetupMask.vert
│  │  │  │  │  │  └── CMakeLists.txt
│  │  │  │  │  ├── CMakeLists.txt
│  │  │  │  │  ├── CubismClass_Vulkan.cpp
│  │  │  │  │  ├── CubismClass_Vulkan.hpp
│  │  │  │  │  ├── CubismOffscreenSurface_Vulkan.cpp
│  │  │  │  │  ├── CubismOffscreenSurface_Vulkan.hpp
│  │  │  │  │  ├── CubismRenderer_Vulkan.cpp
│  │  │  │  │  └── CubismRenderer_Vulkan.hpp
│  │  │  │  ├── CMakeLists.txt
│  │  │  │  ├── CubismClippingManager.hpp
│  │  │  │  ├── CubismClippingManager.tpp
│  │  │  │  ├── CubismRenderer.cpp
│  │  │  │  └── CubismRenderer.hpp
│  │  │  ├── Type
│  │  │  │  ├── CMakeLists.txt
│  │  │  │  ├── csmMap.hpp
│  │  │  │  ├── csmRectF.cpp
│  │  │  │  ├── csmRectF.hpp
│  │  │  │  ├── csmString.cpp
│  │  │  │  ├── csmString.hpp
│  │  │  │  ├── csmVector.hpp
│  │  │  │  └── CubismBasicType.hpp
│  │  │  ├── Utils
│  │  │  │  ├── CMakeLists.txt
│  │  │  │  ├── CubismDebug.cpp
│  │  │  │  ├── CubismDebug.hpp
│  │  │  │  ├── CubismJson.cpp
│  │  │  │  ├── CubismJson.hpp
│  │  │  │  ├── CubismString.cpp
│  │  │  │  └── CubismString.hpp
│  │  │  ├── CMakeLists.txt
│  │  │  ├── CubismCdiJson.cpp
│  │  │  ├── CubismCdiJson.hpp
│  │  │  ├── CubismDefaultParameterId.cpp
│  │  │  ├── CubismDefaultParameterId.hpp
│  │  │  ├── CubismFramework.cpp
│  │  │  ├── CubismFramework.hpp
│  │  │  ├── CubismFrameworkConfig.hpp
│  │  │  ├── CubismJsonHolder.hpp
│  │  │  ├── CubismModelSettingJson.cpp
│  │  │  ├── CubismModelSettingJson.hpp
│  │  │  ├── ICubismAllocator.hpp
│  │  │  ├── ICubismModelSetting.hpp
│  │  │  └── Live2DCubismCore.hpp
│  │  ├── CHANGELOG.md
│  │  ├── CMakeLists.txt
│  │  ├── LICENSE.md
│  │  ├── README.ja.md
│  │  ├── README.md
│  │  └── TRANSLATION.md
│  ├── Samples
│  │  ├── Cocos2d-x
│  │  │  ├── Demo
│  │  │  │  ├── Classes
│  │  │  │  │  ├── AppDelegate.cpp
│  │  │  │  │  ├── AppDelegate.h
│  │  │  │  │  ├── AppMacros.h
│  │  │  │  │  ├── LAppAllocator.cpp
│  │  │  │  │  ├── LAppAllocator.hpp
│  │  │  │  │  ├── LAppDefine.cpp
│  │  │  │  │  ├── LAppDefine.hpp
│  │  │  │  │  ├── LAppLive2DManager.cpp
│  │  │  │  │  ├── LAppLive2DManager.hpp
│  │  │  │  │  ├── LAppLive2DManagerInternal.cpp
│  │  │  │  │  ├── LAppLive2DManagerInternal.h
│  │  │  │  │  ├── LAppModel.cpp
│  │  │  │  │  ├── LAppModel.hpp
│  │  │  │  │  ├── LAppPal.cpp
│  │  │  │  │  ├── LAppPal.hpp
│  │  │  │  │  ├── LAppSprite.cpp
│  │  │  │  │  ├── LAppSprite.hpp
│  │  │  │  │  ├── LAppView.cpp
│  │  │  │  │  ├── LAppView.hpp
│  │  │  │  │  ├── SampleScene.cpp
│  │  │  │  │  ├── SampleScene.h
│  │  │  │  │  ├── TouchManager.cpp
│  │  │  │  │  └── TouchManager.h
│  │  │  │  ├── proj.android
│  │  │  │  │  ├── app
│  │  │  │  │  │  ├── jni
│  │  │  │  │  │  │  └── demo
│  │  │  │  │  │  │     └── main.cpp
│  │  │  │  │  │  ├── res
│  │  │  │  │  │  │  ├── mipmap-hdpi
│  │  │  │  │  │  │  │  └── ic_launcher.png
│  │  │  │  │  │  │  ├── mipmap-mdpi
│  │  │  │  │  │  │  │  └── ic_launcher.png
│  │  │  │  │  │  │  ├── mipmap-xhdpi
│  │  │  │  │  │  │  │  └── ic_launcher.png
│  │  │  │  │  │  │  ├── mipmap-xxhdpi
│  │  │  │  │  │  │  │  └── ic_launcher.png
│  │  │  │  │  │  │  └── values
│  │  │  │  │  │  │     └── strings.xml
│  │  │  │  │  │  ├── src
│  │  │  │  │  │  │  └── org
│  │  │  │  │  │  │     └── cocos2dx
│  │  │  │  │  │  │        └── cpp
│  │  │  │  │  │  │           └── AppActivity.java
│  │  │  │  │  │  ├── AndroidManifest.xml
│  │  │  │  │  │  ├── build.gradle
│  │  │  │  │  │  ├── debug.keystore
│  │  │  │  │  │  └── proguard-rules.pro
│  │  │  │  │  ├── gradle
│  │  │  │  │  │  └── wrapper
│  │  │  │  │  │     ├── gradle-wrapper.jar
│  │  │  │  │  │     └── gradle-wrapper.properties
│  │  │  │  │  ├── build.gradle
│  │  │  │  │  ├── gradle.properties
│  │  │  │  │  ├── gradlew
│  │  │  │  │  ├── gradlew.bat
│  │  │  │  │  └── settings.gradle
│  │  │  │  ├── proj.ios
│  │  │  │  │  ├── scripts
│  │  │  │  │  │  └── proj_xcode
│  │  │  │  │  └── src
│  │  │  │  │     ├── Images.xcassets
│  │  │  │  │     │  ├── AppIcon.appiconset
│  │  │  │  │     │  │  ├── Contents.json
│  │  │  │  │     │  │  ├── Icon-20.png
│  │  │  │  │     │  │  ├── Icon-20@2x.png
│  │  │  │  │     │  │  ├── Icon-20@3x.png
│  │  │  │  │     │  │  ├── Icon-29.png
│  │  │  │  │     │  │  ├── Icon-29@2x.png
│  │  │  │  │     │  │  ├── Icon-29@3x.png
│  │  │  │  │     │  │  ├── Icon-40.png
│  │  │  │  │     │  │  ├── Icon-40@2x.png
│  │  │  │  │     │  │  ├── Icon-40@3x.png
│  │  │  │  │     │  │  ├── Icon-50.png
│  │  │  │  │     │  │  ├── Icon-50@2x.png
│  │  │  │  │     │  │  ├── Icon-57.png
│  │  │  │  │     │  │  ├── Icon-57@2x.png
│  │  │  │  │     │  │  ├── Icon-60@2x.png
│  │  │  │  │     │  │  ├── Icon-60@3x.png
│  │  │  │  │     │  │  ├── Icon-72.png
│  │  │  │  │     │  │  ├── Icon-72@2x.png
│  │  │  │  │     │  │  ├── Icon-76.png
│  │  │  │  │     │  │  ├── Icon-76@2x.png
│  │  │  │  │     │  │  └── Icon-83.5@2x.png
│  │  │  │  │     │  └── Contents.json
│  │  │  │  │     ├── AppController.h
│  │  │  │  │     ├── AppController.mm
│  │  │  │  │     ├── exportoptions.plist
│  │  │  │  │     ├── Info.plist
│  │  │  │  │     ├── LaunchScreen.storyboard
│  │  │  │  │     ├── LaunchScreenBackground.png
│  │  │  │  │     ├── main.m
│  │  │  │  │     ├── Prefix.pch
│  │  │  │  │     ├── RootViewController.h
│  │  │  │  │     └── RootViewController.mm
│  │  │  │  ├── proj.linux
│  │  │  │  │  ├── scripts
│  │  │  │  │  │  ├── fix_libs
│  │  │  │  │  │  └── make_gcc
│  │  │  │  │  └── src
│  │  │  │  │     └── main.cpp
│  │  │  │  ├── proj.mac
│  │  │  │  │  ├── scripts
│  │  │  │  │  │  ├── make_xcode
│  │  │  │  │  │  └── proj_xcode
│  │  │  │  │  └── src
│  │  │  │  │     ├── Icon.icns
│  │  │  │  │     ├── Info.plist
│  │  │  │  │     ├── main.cpp
│  │  │  │  │     └── Prefix.pch
│  │  │  │  ├── proj.win
│  │  │  │  │  ├── scripts
│  │  │  │  │  │  ├── proj_msvc2015.bat
│  │  │  │  │  │  ├── proj_msvc2017.bat
│  │  │  │  │  │  ├── proj_msvc2019.bat
│  │  │  │  │  │  ├── proj_msvc2022.bat
│  │  │  │  │  │  └── _msvc_common.bat
│  │  │  │  │  └── src
│  │  │  │  │     ├── res
│  │  │  │  │     │  └── game.ico
│  │  │  │  │     ├── game.rc
│  │  │  │  │     ├── main.cpp
│  │  │  │  │     ├── main.h
│  │  │  │  │     └── resource.h
│  │  │  │  ├── Resources
│  │  │  │  │  ├── fonts
│  │  │  │  │  │  ├── arial.ttf
│  │  │  │  │  │  └── Marker Felt.ttf
│  │  │  │  │  ├── res
│  │  │  │  │  │  └── .gitkeep
│  │  │  │  │  ├── CloseNormal.png
│  │  │  │  │  ├── CloseSelected.png
│  │  │  │  │  └── HelloWorld.png
│  │  │  │  └── CMakeLists.txt
│  │  │  ├── thirdParty
│  │  │  │  └── scripts
│  │  │  │     ├── setup_cocos2d
│  │  │  │     └── setup_cocos2d.bat
│  │  │  ├── README.ja.md
│  │  │  └── README.md
│  │  ├── D3D11
│  │  │  ├── Demo
│  │  │  │  └── proj.d3d11.cmake
│  │  │  │     ├── scripts
│  │  │  │     │  ├── nmake_msvc2013.bat
│  │  │  │     │  ├── nmake_msvc2015.bat
│  │  │  │     │  ├── nmake_msvc2017.bat
│  │  │  │     │  ├── nmake_msvc2019.bat
│  │  │  │     │  ├── nmake_msvc2022.bat
│  │  │  │     │  ├── proj_msvc2013.bat
│  │  │  │     │  ├── proj_msvc2015.bat
│  │  │  │     │  ├── proj_msvc2017.bat
│  │  │  │     │  ├── proj_msvc2019.bat
│  │  │  │     │  ├── proj_msvc2022.bat
│  │  │  │     │  └── _msvc_common.bat
│  │  │  │     ├── src
│  │  │  │     │  ├── CMakeLists.txt
│  │  │  │     │  ├── CubismDirectXRenderer.cpp
│  │  │  │     │  ├── CubismDirectXRenderer.hpp
│  │  │  │     │  ├── CubismDirectXView.cpp
│  │  │  │     │  ├── CubismDirectXView.hpp
│  │  │  │     │  ├── CubismSampleViewMatrix.cpp
│  │  │  │     │  ├── CubismSampleViewMatrix.hpp
│  │  │  │     │  ├── CubismSprite.cpp
│  │  │  │     │  ├── CubismSprite.hpp
│  │  │  │     │  ├── CubismTextureManager.cpp
│  │  │  │     │  ├── CubismTextureManager.hpp
│  │  │  │     │  ├── CubismUserModelExtend.cpp
│  │  │  │     │  ├── CubismUserModelExtend.hpp
│  │  │  │     │  ├── LAppAllocator.cpp
│  │  │  │     │  ├── LAppAllocator.hpp
│  │  │  │     │  ├── LAppDefine.cpp
│  │  │  │     │  ├── LAppDefine.hpp
│  │  │  │     │  ├── LAppDelegate.cpp
│  │  │  │     │  ├── LAppDelegate.hpp
│  │  │  │     │  ├── LAppLive2DManager.cpp
│  │  │  │     │  ├── LAppLive2DManager.hpp
│  │  │  │     │  ├── LAppModel.cpp
│  │  │  │     │  ├── LAppModel.hpp
│  │  │  │     │  ├── LAppPal.cpp
│  │  │  │     │  ├── LAppPal.hpp
│  │  │  │     │  ├── LAppSprite.cpp
│  │  │  │     │  ├── LAppSprite.hpp
│  │  │  │     │  ├── LAppTextureManager.cpp
│  │  │  │     │  ├── LAppTextureManager.hpp
│  │  │  │     │  ├── LAppView.cpp
│  │  │  │     │  ├── LAppView.hpp
│  │  │  │     │  ├── LAppWavFileHandler.cpp
│  │  │  │     │  ├── LAppWavFileHandler.hpp
│  │  │  │     │  ├── main.cpp
│  │  │  │     │  ├── mainMinimum.cpp
│  │  │  │     │  ├── MouseActionManager.cpp
│  │  │  │     │  ├── MouseActionManager.hpp
│  │  │  │     │  ├── TouchManager.cpp
│  │  │  │     │  └── TouchManager.hpp
│  │  │  │     └── CMakeLists.txt
│  │  │  ├── thirdParty
│  │  │  │  └── scripts
│  │  │  │     ├── setup_msvc2013.bat
│  │  │  │     ├── setup_msvc2015.bat
│  │  │  │     ├── setup_msvc2017.bat
│  │  │  │     ├── setup_msvc2019.bat
│  │  │  │     ├── setup_msvc2022.bat
│  │  │  │     ├── _msvc_common.bat
│  │  │  │     └── _setup_common.bat
│  │  │  ├── README.ja.md
│  │  │  └── README.md
│  │  ├── D3D9
│  │  │  ├── Demo
│  │  │  │  └── proj.d3d9.cmake
│  │  │  │     ├── scripts
│  │  │  │     │  ├── nmake_msvc2013.bat
│  │  │  │     │  ├── nmake_msvc2015.bat
│  │  │  │     │  ├── nmake_msvc2017.bat
│  │  │  │     │  ├── nmake_msvc2019.bat
│  │  │  │     │  ├── nmake_msvc2022.bat
│  │  │  │     │  ├── proj_msvc2013.bat
│  │  │  │     │  ├── proj_msvc2015.bat
│  │  │  │     │  ├── proj_msvc2017.bat
│  │  │  │     │  ├── proj_msvc2019.bat
│  │  │  │     │  ├── proj_msvc2022.bat
│  │  │  │     │  └── _msvc_common.bat
│  │  │  │     ├── src
│  │  │  │     │  ├── CMakeLists.txt
│  │  │  │     │  ├── CubismDirectXRenderer.cpp
│  │  │  │     │  ├── CubismDirectXRenderer.hpp
│  │  │  │     │  ├── CubismDirectXView.cpp
│  │  │  │     │  ├── CubismDirectXView.hpp
│  │  │  │     │  ├── CubismSampleViewMatrix.cpp
│  │  │  │     │  ├── CubismSampleViewMatrix.hpp
│  │  │  │     │  ├── CubismSprite.cpp
│  │  │  │     │  ├── CubismSprite.hpp
│  │  │  │     │  ├── CubismTextureManager.cpp
│  │  │  │     │  ├── CubismTextureManager.hpp
│  │  │  │     │  ├── CubismUserModelExtend.cpp
│  │  │  │     │  ├── CubismUserModelExtend.hpp
│  │  │  │     │  ├── LAppAllocator.cpp
│  │  │  │     │  ├── LAppAllocator.hpp
│  │  │  │     │  ├── LAppDefine.cpp
│  │  │  │     │  ├── LAppDefine.hpp
│  │  │  │     │  ├── LAppDelegate.cpp
│  │  │  │     │  ├── LAppDelegate.hpp
│  │  │  │     │  ├── LAppLive2DManager.cpp
│  │  │  │     │  ├── LAppLive2DManager.hpp
│  │  │  │     │  ├── LAppModel.cpp
│  │  │  │     │  ├── LAppModel.hpp
│  │  │  │     │  ├── LAppPal.cpp
│  │  │  │     │  ├── LAppPal.hpp
│  │  │  │     │  ├── LAppSprite.cpp
│  │  │  │     │  ├── LAppSprite.hpp
│  │  │  │     │  ├── LAppTextureManager.cpp
│  │  │  │     │  ├── LAppTextureManager.hpp
│  │  │  │     │  ├── LAppView.cpp
│  │  │  │     │  ├── LAppView.hpp
│  │  │  │     │  ├── LAppWavFileHandler.cpp
│  │  │  │     │  ├── LAppWavFileHandler.hpp
│  │  │  │     │  ├── main.cpp
│  │  │  │     │  ├── mainMinimum.cpp
│  │  │  │     │  ├── MouseActionManager.cpp
│  │  │  │     │  ├── MouseActionManager.hpp
│  │  │  │     │  ├── TouchManager.cpp
│  │  │  │     │  └── TouchManager.hpp
│  │  │  │     └── CMakeLists.txt
│  │  │  ├── README.ja.md
│  │  │  └── README.md
│  │  ├── Metal
│  │  │  ├── Demo
│  │  │  │  └── proj.ios.cmake
│  │  │  │     ├── scripts
│  │  │  │     │  └── proj_xcode
│  │  │  │     ├── src
│  │  │  │     │  ├── AppDelegate.h
│  │  │  │     │  ├── AppDelegate.mm
│  │  │  │     │  ├── CMakeLists.txt
│  │  │  │     │  ├── Info.plist
│  │  │  │     │  ├── LAppAllocator.h
│  │  │  │     │  ├── LAppAllocator.mm
│  │  │  │     │  ├── LAppDefine.h
│  │  │  │     │  ├── LAppDefine.mm
│  │  │  │     │  ├── LAppLive2DManager.h
│  │  │  │     │  ├── LAppLive2DManager.mm
│  │  │  │     │  ├── LAppModel.h
│  │  │  │     │  ├── LAppModel.mm
│  │  │  │     │  ├── LAppPal.h
│  │  │  │     │  ├── LAppPal.mm
│  │  │  │     │  ├── LAppSprite.h
│  │  │  │     │  ├── LAppSprite.mm
│  │  │  │     │  ├── LAppTextureManager.h
│  │  │  │     │  ├── LAppTextureManager.mm
│  │  │  │     │  ├── main.m
│  │  │  │     │  ├── MetalConfig.h
│  │  │  │     │  ├── MetalUIView.h
│  │  │  │     │  ├── MetalUIView.m
│  │  │  │     │  ├── MetalView.h
│  │  │  │     │  ├── MetalView.m
│  │  │  │     │  ├── TouchManager.h
│  │  │  │     │  ├── TouchManager.mm
│  │  │  │     │  ├── ViewController.h
│  │  │  │     │  └── ViewController.mm
│  │  │  │     └── CMakeLists.txt
│  │  │  ├── thirdParty
│  │  │  │  ├── scripts
│  │  │  │  │  └── setup_ios_cmake
│  │  │  │  └── stb
│  │  │  │     ├── README.md
│  │  │  │     └── stb_image.h
│  │  │  ├── README.ja.md
│  │  │  └── README.md
│  │  ├── OpenGL
│  │  │  ├── Demo
│  │  │  │  ├── proj.android.cmake
│  │  │  │  │  ├── Full
│  │  │  │  │  │  ├── app
│  │  │  │  │  │  │  ├── src
│  │  │  │  │  │  │  │  └── main
│  │  │  │  │  │  │  │     ├── cpp
│  │  │  │  │  │  │  │     │  ├── CMakeLists.txt
│  │  │  │  │  │  │  │     │  ├── JniBridgeC.cpp
│  │  │  │  │  │  │  │     │  ├── JniBridgeC.hpp
│  │  │  │  │  │  │  │     │  ├── LAppAllocator.cpp
│  │  │  │  │  │  │  │     │  ├── LAppAllocator.hpp
│  │  │  │  │  │  │  │     │  ├── LAppDefine.cpp
│  │  │  │  │  │  │  │     │  ├── LAppDefine.hpp
│  │  │  │  │  │  │  │     │  ├── LAppDelegate.cpp
│  │  │  │  │  │  │  │     │  ├── LAppDelegate.hpp
│  │  │  │  │  │  │  │     │  ├── LAppLive2DManager.cpp
│  │  │  │  │  │  │  │     │  ├── LAppLive2DManager.hpp
│  │  │  │  │  │  │  │     │  ├── LAppModel.cpp
│  │  │  │  │  │  │  │     │  ├── LAppModel.hpp
│  │  │  │  │  │  │  │     │  ├── LAppPal.cpp
│  │  │  │  │  │  │  │     │  ├── LAppPal.hpp
│  │  │  │  │  │  │  │     │  ├── LAppSprite.cpp
│  │  │  │  │  │  │  │     │  ├── LAppSprite.hpp
│  │  │  │  │  │  │  │     │  ├── LAppTextureManager.cpp
│  │  │  │  │  │  │  │     │  ├── LAppTextureManager.hpp
│  │  │  │  │  │  │  │     │  ├── LAppView.cpp
│  │  │  │  │  │  │  │     │  ├── LAppView.hpp
│  │  │  │  │  │  │  │     │  ├── LAppWavFileHandler.cpp
│  │  │  │  │  │  │  │     │  ├── LAppWavFileHandler.hpp
│  │  │  │  │  │  │  │     │  ├── TouchManager.cpp
│  │  │  │  │  │  │  │     │  └── TouchManager.hpp
│  │  │  │  │  │  │  │     ├── java
│  │  │  │  │  │  │  │     │  └── com
│  │  │  │  │  │  │  │     │     └── live2d
│  │  │  │  │  │  │  │     │        └── demo
│  │  │  │  │  │  │  │     │           ├── GLRenderer.java
│  │  │  │  │  │  │  │     │           ├── JniBridgeJava.java
│  │  │  │  │  │  │  │     │           └── MainActivity.java
│  │  │  │  │  │  │  │     ├── res
│  │  │  │  │  │  │  │     │  ├── drawable
│  │  │  │  │  │  │  │     │  │  └── ic_launcher_background.xml
│  │  │  │  │  │  │  │     │  ├── drawable-v24
│  │  │  │  │  │  │  │     │  │  └── ic_launcher_foreground.xml
│  │  │  │  │  │  │  │     │  ├── layout
│  │  │  │  │  │  │  │     │  │  └── activity_main.xml
│  │  │  │  │  │  │  │     │  ├── mipmap-anydpi-v26
│  │  │  │  │  │  │  │     │  │  ├── ic_launcher.xml
│  │  │  │  │  │  │  │     │  │  └── ic_launcher_round.xml
│  │  │  │  │  │  │  │     │  ├── mipmap-hdpi
│  │  │  │  │  │  │  │     │  │  ├── ic_launcher.png
│  │  │  │  │  │  │  │     │  │  └── ic_launcher_round.png
│  │  │  │  │  │  │  │     │  ├── mipmap-mdpi
│  │  │  │  │  │  │  │     │  │  ├── ic_launcher.png
│  │  │  │  │  │  │  │     │  │  └── ic_launcher_round.png
│  │  │  │  │  │  │  │     │  ├── mipmap-xhdpi
│  │  │  │  │  │  │  │     │  │  ├── ic_launcher.png
│  │  │  │  │  │  │  │     │  │  └── ic_launcher_round.png
│  │  │  │  │  │  │  │     │  ├── mipmap-xxhdpi
│  │  │  │  │  │  │  │     │  │  ├── ic_launcher.png
│  │  │  │  │  │  │  │     │  │  └── ic_launcher_round.png
│  │  │  │  │  │  │  │     │  ├── mipmap-xxxhdpi
│  │  │  │  │  │  │  │     │  │  ├── ic_launcher.png
│  │  │  │  │  │  │  │     │  │  └── ic_launcher_round.png
│  │  │  │  │  │  │  │     │  └── values
│  │  │  │  │  │  │  │     │     ├── colors.xml
│  │  │  │  │  │  │  │     │     ├── strings.xml
│  │  │  │  │  │  │  │     │     └── styles.xml
│  │  │  │  │  │  │  │     └── AndroidManifest.xml
│  │  │  │  │  │  │  ├── build.gradle
│  │  │  │  │  │  │  ├── CMakeLists.txt
│  │  │  │  │  │  │  ├── debug.keystore
│  │  │  │  │  │  │  └── proguard-rules.pro
│  │  │  │  │  │  ├── gradle
│  │  │  │  │  │  │  └── wrapper
│  │  │  │  │  │  │     ├── gradle-wrapper.jar
│  │  │  │  │  │  │     └── gradle-wrapper.properties
│  │  │  │  │  │  ├── build.gradle
│  │  │  │  │  │  ├── gradle.properties
│  │  │  │  │  │  ├── gradlew
│  │  │  │  │  │  ├── gradlew.bat
│  │  │  │  │  │  └── settings.gradle
│  │  │  │  │  └── Minimum
│  │  │  │  │     ├── app
│  │  │  │  │     │  ├── src
│  │  │  │  │     │  │  └── main
│  │  │  │  │     │  │     ├── cpp
│  │  │  │  │     │  │     │  ├── CMakeLists.txt
│  │  │  │  │     │  │     │  ├── JniBridgeC.cpp
│  │  │  │  │     │  │     │  ├── JniBridgeC.hpp
│  │  │  │  │     │  │     │  ├── LAppAllocator.cpp
│  │  │  │  │     │  │     │  ├── LAppAllocator.hpp
│  │  │  │  │     │  │     │  ├── LAppDefine.cpp
│  │  │  │  │     │  │     │  ├── LAppDefine.hpp
│  │  │  │  │     │  │     │  ├── LAppMinimumDelegate.cpp
│  │  │  │  │     │  │     │  ├── LAppMinimumDelegate.hpp
│  │  │  │  │     │  │     │  ├── LAppMinimumLive2DManager.cpp
│  │  │  │  │     │  │     │  ├── LAppMinimumLive2DManager.hpp
│  │  │  │  │     │  │     │  ├── LAppMinimumModel.cpp
│  │  │  │  │     │  │     │  ├── LAppMinimumModel.hpp
│  │  │  │  │     │  │     │  ├── LAppMinimumView.cpp
│  │  │  │  │     │  │     │  ├── LAppMinimumView.hpp
│  │  │  │  │     │  │     │  ├── LAppPal.cpp
│  │  │  │  │     │  │     │  ├── LAppPal.hpp
│  │  │  │  │     │  │     │  ├── LAppSprite.cpp
│  │  │  │  │     │  │     │  ├── LAppSprite.hpp
│  │  │  │  │     │  │     │  ├── LAppTextureManager.cpp
│  │  │  │  │     │  │     │  ├── LAppTextureManager.hpp
│  │  │  │  │     │  │     │  ├── LAppWavFileHandler.cpp
│  │  │  │  │     │  │     │  ├── LAppWavFileHandler.hpp
│  │  │  │  │     │  │     │  ├── TouchManager.cpp
│  │  │  │  │     │  │     │  └── TouchManager.hpp
│  │  │  │  │     │  │     ├── java
│  │  │  │  │     │  │     │  └── com
│  │  │  │  │     │  │     │     └── live2d
│  │  │  │  │     │  │     │        └── demo
│  │  │  │  │     │  │     │           ├── GLRenderer.java
│  │  │  │  │     │  │     │           ├── JniBridgeJava.java
│  │  │  │  │     │  │     │           └── MainActivity.java
│  │  │  │  │     │  │     ├── res
│  │  │  │  │     │  │     │  ├── drawable
│  │  │  │  │     │  │     │  │  └── ic_launcher_background.xml
│  │  │  │  │     │  │     │  ├── drawable-v24
│  │  │  │  │     │  │     │  │  └── ic_launcher_foreground.xml
│  │  │  │  │     │  │     │  ├── layout
│  │  │  │  │     │  │     │  │  └── activity_main.xml
│  │  │  │  │     │  │     │  ├── mipmap-anydpi-v26
│  │  │  │  │     │  │     │  │  ├── ic_launcher.xml
│  │  │  │  │     │  │     │  │  └── ic_launcher_round.xml
│  │  │  │  │     │  │     │  ├── mipmap-hdpi
│  │  │  │  │     │  │     │  │  ├── ic_launcher.png
│  │  │  │  │     │  │     │  │  └── ic_launcher_round.png
│  │  │  │  │     │  │     │  ├── mipmap-mdpi
│  │  │  │  │     │  │     │  │  ├── ic_launcher.png
│  │  │  │  │     │  │     │  │  └── ic_launcher_round.png
│  │  │  │  │     │  │     │  ├── mipmap-xhdpi
│  │  │  │  │     │  │     │  │  ├── ic_launcher.png
│  │  │  │  │     │  │     │  │  └── ic_launcher_round.png
│  │  │  │  │     │  │     │  ├── mipmap-xxhdpi
│  │  │  │  │     │  │     │  │  ├── ic_launcher.png
│  │  │  │  │     │  │     │  │  └── ic_launcher_round.png
│  │  │  │  │     │  │     │  ├── mipmap-xxxhdpi
│  │  │  │  │     │  │     │  │  ├── ic_launcher.png
│  │  │  │  │     │  │     │  │  └── ic_launcher_round.png
│  │  │  │  │     │  │     │  └── values
│  │  │  │  │     │  │     │     ├── colors.xml
│  │  │  │  │     │  │     │     ├── strings.xml
│  │  │  │  │     │  │     │     └── styles.xml
│  │  │  │  │     │  │     └── AndroidManifest.xml
│  │  │  │  │     │  ├── build.gradle
│  │  │  │  │     │  ├── CMakeLists.txt
│  │  │  │  │     │  ├── debug.keystore
│  │  │  │  │     │  ├── local.properties
│  │  │  │  │     │  └── proguard-rules.pro
│  │  │  │  │     ├── gradle
│  │  │  │  │     │  └── wrapper
│  │  │  │  │     │     ├── gradle-wrapper.jar
│  │  │  │  │     │     └── gradle-wrapper.properties
│  │  │  │  │     ├── build.gradle
│  │  │  │  │     ├── gradle.properties
│  │  │  │  │     ├── gradlew
│  │  │  │  │     ├── gradlew.bat
│  │  │  │  │     └── settings.gradle
│  │  │  │  ├── proj.ios.cmake
│  │  │  │  │  ├── scripts
│  │  │  │  │  │  └── proj_xcode
│  │  │  │  │  ├── src
│  │  │  │  │  │  ├── minimum
│  │  │  │  │  │  │  ├── MinAppDelegate.h
│  │  │  │  │  │  │  ├── MinAppDelegate.mm
│  │  │  │  │  │  │  ├── MinimumMain.m
│  │  │  │  │  │  │  ├── MinLAppAllocator.h
│  │  │  │  │  │  │  ├── MinLAppAllocator.mm
│  │  │  │  │  │  │  ├── MinLAppDefine.h
│  │  │  │  │  │  │  ├── MinLAppDefine.mm
│  │  │  │  │  │  │  ├── MinLAppLive2DManager.h
│  │  │  │  │  │  │  ├── MinLAppLive2DManager.mm
│  │  │  │  │  │  │  ├── MinLAppModel.h
│  │  │  │  │  │  │  ├── MinLAppModel.mm
│  │  │  │  │  │  │  ├── MinLAppPal.h
│  │  │  │  │  │  │  ├── MinLAppPal.mm
│  │  │  │  │  │  │  ├── MinLAppSprite.h
│  │  │  │  │  │  │  ├── MinLAppSprite.mm
│  │  │  │  │  │  │  ├── MinLAppTextureManager.h
│  │  │  │  │  │  │  ├── MinLAppTextureManager.mm
│  │  │  │  │  │  │  ├── MinTouchManager.h
│  │  │  │  │  │  │  ├── MinTouchManager.mm
│  │  │  │  │  │  │  ├── MinViewController.h
│  │  │  │  │  │  │  └── MinViewController.mm
│  │  │  │  │  │  ├── AppDelegate.h
│  │  │  │  │  │  ├── AppDelegate.mm
│  │  │  │  │  │  ├── CMakeLists.txt
│  │  │  │  │  │  ├── Info.plist
│  │  │  │  │  │  ├── LAppAllocator.h
│  │  │  │  │  │  ├── LAppAllocator.mm
│  │  │  │  │  │  ├── LAppDefine.h
│  │  │  │  │  │  ├── LAppDefine.mm
│  │  │  │  │  │  ├── LAppLive2DManager.h
│  │  │  │  │  │  ├── LAppLive2DManager.mm
│  │  │  │  │  │  ├── LAppModel.h
│  │  │  │  │  │  ├── LAppModel.mm
│  │  │  │  │  │  ├── LAppPal.h
│  │  │  │  │  │  ├── LAppPal.mm
│  │  │  │  │  │  ├── LAppSprite.h
│  │  │  │  │  │  ├── LAppSprite.mm
│  │  │  │  │  │  ├── LAppTextureManager.h
│  │  │  │  │  │  ├── LAppTextureManager.mm
│  │  │  │  │  │  ├── LAppWavFileHandler.h
│  │  │  │  │  │  ├── LAppWavFileHandler.mm
│  │  │  │  │  │  ├── main.m
│  │  │  │  │  │  ├── TouchManager.h
│  │  │  │  │  │  ├── TouchManager.mm
│  │  │  │  │  │  ├── ViewController.h
│  │  │  │  │  │  └── ViewController.mm
│  │  │  │  │  └── CMakeLists.txt
│  │  │  │  ├── proj.linux.cmake
│  │  │  │  │  ├── scripts
│  │  │  │  │  │  └── make_gcc
│  │  │  │  │  ├── src
│  │  │  │  │  │  ├── CMakeLists.txt
│  │  │  │  │  │  ├── CubismSampleViewMatrix.cpp
│  │  │  │  │  │  ├── CubismSampleViewMatrix.hpp
│  │  │  │  │  │  ├── CubismUserModelExtend.cpp
│  │  │  │  │  │  ├── CubismUserModelExtend.hpp
│  │  │  │  │  │  ├── LAppAllocator.cpp
│  │  │  │  │  │  ├── LAppAllocator.hpp
│  │  │  │  │  │  ├── LAppDefine.cpp
│  │  │  │  │  │  ├── LAppDefine.hpp
│  │  │  │  │  │  ├── LAppDelegate.cpp
│  │  │  │  │  │  ├── LAppDelegate.hpp
│  │  │  │  │  │  ├── LAppLive2DManager.cpp
│  │  │  │  │  │  ├── LAppLive2DManager.hpp
│  │  │  │  │  │  ├── LAppModel.cpp
│  │  │  │  │  │  ├── LAppModel.hpp
│  │  │  │  │  │  ├── LAppPal.cpp
│  │  │  │  │  │  ├── LAppPal.hpp
│  │  │  │  │  │  ├── LAppSprite.cpp
│  │  │  │  │  │  ├── LAppSprite.hpp
│  │  │  │  │  │  ├── LAppTextureManager.cpp
│  │  │  │  │  │  ├── LAppTextureManager.hpp
│  │  │  │  │  │  ├── LAppView.cpp
│  │  │  │  │  │  ├── LAppView.hpp
│  │  │  │  │  │  ├── LAppWavFileHandler.cpp
│  │  │  │  │  │  ├── LAppWavFileHandler.hpp
│  │  │  │  │  │  ├── main.cpp
│  │  │  │  │  │  ├── mainMinimum.cpp
│  │  │  │  │  │  ├── MouseActionManager.cpp
│  │  │  │  │  │  ├── MouseActionManager.hpp
│  │  │  │  │  │  ├── TouchManager.cpp
│  │  │  │  │  │  └── TouchManager.hpp
│  │  │  │  │  └── CMakeLists.txt
│  │  │  │  ├── proj.mac.cmake
│  │  │  │  │  ├── scripts
│  │  │  │  │  │  ├── make_xcode
│  │  │  │  │  │  └── proj_xcode
│  │  │  │  │  ├── src
│  │  │  │  │  │  ├── CMakeLists.txt
│  │  │  │  │  │  ├── CubismSampleViewMatrix.cpp
│  │  │  │  │  │  ├── CubismSampleViewMatrix.hpp
│  │  │  │  │  │  ├── CubismUserModelExtend.cpp
│  │  │  │  │  │  ├── CubismUserModelExtend.hpp
│  │  │  │  │  │  ├── LAppAllocator.cpp
│  │  │  │  │  │  ├── LAppAllocator.hpp
│  │  │  │  │  │  ├── LAppDefine.cpp
│  │  │  │  │  │  ├── LAppDefine.hpp
│  │  │  │  │  │  ├── LAppDelegate.cpp
│  │  │  │  │  │  ├── LAppDelegate.hpp
│  │  │  │  │  │  ├── LAppLive2DManager.cpp
│  │  │  │  │  │  ├── LAppLive2DManager.hpp
│  │  │  │  │  │  ├── LAppModel.cpp
│  │  │  │  │  │  ├── LAppModel.hpp
│  │  │  │  │  │  ├── LAppPal.cpp
│  │  │  │  │  │  ├── LAppPal.hpp
│  │  │  │  │  │  ├── LAppSprite.cpp
│  │  │  │  │  │  ├── LAppSprite.hpp
│  │  │  │  │  │  ├── LAppTextureManager.cpp
│  │  │  │  │  │  ├── LAppTextureManager.hpp
│  │  │  │  │  │  ├── LAppView.cpp
│  │  │  │  │  │  ├── LAppView.hpp
│  │  │  │  │  │  ├── LAppWavFileHandler.cpp
│  │  │  │  │  │  ├── LAppWavFileHandler.hpp
│  │  │  │  │  │  ├── main.cpp
│  │  │  │  │  │  ├── mainMinimum.cpp
│  │  │  │  │  │  ├── MouseActionManager.cpp
│  │  │  │  │  │  ├── MouseActionManager.hpp
│  │  │  │  │  │  ├── TouchManager.cpp
│  │  │  │  │  │  └── TouchManager.hpp
│  │  │  │  │  └── CMakeLists.txt
│  │  │  │  └── proj.win.cmake
│  │  │  │     ├── scripts
│  │  │  │     │  ├── nmake_msvc2013.bat
│  │  │  │     │  ├── nmake_msvc2015.bat
│  │  │  │     │  ├── nmake_msvc2017.bat
│  │  │  │     │  ├── nmake_msvc2019.bat
│  │  │  │     │  ├── nmake_msvc2022.bat
│  │  │  │     │  ├── proj_msvc2013.bat
│  │  │  │     │  ├── proj_msvc2015.bat
│  │  │  │     │  ├── proj_msvc2017.bat
│  │  │  │     │  ├── proj_msvc2019.bat
│  │  │  │     │  ├── proj_msvc2022.bat
│  │  │  │     │  └── _msvc_common.bat
│  │  │  │     ├── src
│  │  │  │     │  ├── CMakeLists.txt
│  │  │  │     │  ├── CubismSampleViewMatrix.cpp
│  │  │  │     │  ├── CubismSampleViewMatrix.hpp
│  │  │  │     │  ├── CubismUserModelExtend.cpp
│  │  │  │     │  ├── CubismUserModelExtend.hpp
│  │  │  │     │  ├── LAppAllocator.cpp
│  │  │  │     │  ├── LAppAllocator.hpp
│  │  │  │     │  ├── LAppDefine.cpp
│  │  │  │     │  ├── LAppDefine.hpp
│  │  │  │     │  ├── LAppDelegate.cpp
│  │  │  │     │  ├── LAppDelegate.hpp
│  │  │  │     │  ├── LAppLive2DManager.cpp
│  │  │  │     │  ├── LAppLive2DManager.hpp
│  │  │  │     │  ├── LAppModel.cpp
│  │  │  │     │  ├── LAppModel.hpp
│  │  │  │     │  ├── LAppPal.cpp
│  │  │  │     │  ├── LAppPal.hpp
│  │  │  │     │  ├── LAppSprite.cpp
│  │  │  │     │  ├── LAppSprite.hpp
│  │  │  │     │  ├── LAppTextureManager.cpp
│  │  │  │     │  ├── LAppTextureManager.hpp
│  │  │  │     │  ├── LAppView.cpp
│  │  │  │     │  ├── LAppView.hpp
│  │  │  │     │  ├── LAppWavFileHandler.cpp
│  │  │  │     │  ├── LAppWavFileHandler.hpp
│  │  │  │     │  ├── main.cpp
│  │  │  │     │  ├── mainMinimum.cpp
│  │  │  │     │  ├── MouseActionManager.cpp
│  │  │  │     │  ├── MouseActionManager.hpp
│  │  │  │     │  ├── TouchManager.cpp
│  │  │  │     │  └── TouchManager.hpp
│  │  │  │     └── CMakeLists.txt
│  │  │  ├── thirdParty
│  │  │  │  ├── scripts
│  │  │  │  │  ├── setup_glew_glfw
│  │  │  │  │  ├── setup_glew_glfw.bat
│  │  │  │  │  ├── setup_glew_glfw_vs2013.bat
│  │  │  │  │  └── setup_ios_cmake
│  │  │  │  └── stb
│  │  │  │     ├── README.md
│  │  │  │     └── stb_image.h
│  │  │  ├── README.ja.md
│  │  │  └── README.md
│  │  ├── Resources
│  │  │  ├── Haru
│  │  │  │  ├── expressions
│  │  │  │  │  ├── F01.exp3.json
│  │  │  │  │  ├── F02.exp3.json
│  │  │  │  │  ├── F03.exp3.json
│  │  │  │  │  ├── F04.exp3.json
│  │  │  │  │  ├── F05.exp3.json
│  │  │  │  │  ├── F06.exp3.json
│  │  │  │  │  ├── F07.exp3.json
│  │  │  │  │  └── F08.exp3.json
│  │  │  │  ├── Haru.2048
│  │  │  │  │  ├── texture_00.png
│  │  │  │  │  └── texture_01.png
│  │  │  │  ├── motions
│  │  │  │  │  ├── haru_g_idle.motion3.json
│  │  │  │  │  ├── haru_g_m01.motion3.json
│  │  │  │  │  ├── haru_g_m02.motion3.json
│  │  │  │  │  ├── haru_g_m03.motion3.json
│  │  │  │  │  ├── haru_g_m04.motion3.json
│  │  │  │  │  ├── haru_g_m05.motion3.json
│  │  │  │  │  ├── haru_g_m06.motion3.json
│  │  │  │  │  ├── haru_g_m07.motion3.json
│  │  │  │  │  ├── haru_g_m08.motion3.json
│  │  │  │  │  ├── haru_g_m09.motion3.json
│  │  │  │  │  ├── haru_g_m10.motion3.json
│  │  │  │  │  ├── haru_g_m11.motion3.json
│  │  │  │  │  ├── haru_g_m12.motion3.json
│  │  │  │  │  ├── haru_g_m13.motion3.json
│  │  │  │  │  ├── haru_g_m14.motion3.json
│  │  │  │  │  ├── haru_g_m15.motion3.json
│  │  │  │  │  ├── haru_g_m16.motion3.json
│  │  │  │  │  ├── haru_g_m17.motion3.json
│  │  │  │  │  ├── haru_g_m18.motion3.json
│  │  │  │  │  ├── haru_g_m19.motion3.json
│  │  │  │  │  ├── haru_g_m20.motion3.json
│  │  │  │  │  ├── haru_g_m21.motion3.json
│  │  │  │  │  ├── haru_g_m22.motion3.json
│  │  │  │  │  ├── haru_g_m23.motion3.json
│  │  │  │  │  ├── haru_g_m24.motion3.json
│  │  │  │  │  ├── haru_g_m25.motion3.json
│  │  │  │  │  └── haru_g_m26.motion3.json
│  │  │  │  ├── sounds
│  │  │  │  │  ├── haru_Info_04.wav
│  │  │  │  │  ├── haru_Info_14.wav
│  │  │  │  │  ├── haru_normal_6.wav
│  │  │  │  │  └── haru_talk_13.wav
│  │  │  │  ├── Haru.cdi3.json
│  │  │  │  ├── Haru.moc3
│  │  │  │  ├── Haru.model3.json
│  │  │  │  ├── Haru.physics3.json
│  │  │  │  ├── Haru.pose3.json
│  │  │  │  └── Haru.userdata3.json
│  │  │  ├── Hiyori
│  │  │  │  ├── Hiyori.2048
│  │  │  │  │  ├── texture_00.png
│  │  │  │  │  └── texture_01.png
│  │  │  │  ├── motions
│  │  │  │  │  ├── Hiyori_m01.motion3.json
│  │  │  │  │  ├── Hiyori_m02.motion3.json
│  │  │  │  │  ├── Hiyori_m03.motion3.json
│  │  │  │  │  ├── Hiyori_m04.motion3.json
│  │  │  │  │  ├── Hiyori_m05.motion3.json
│  │  │  │  │  ├── Hiyori_m06.motion3.json
│  │  │  │  │  ├── Hiyori_m07.motion3.json
│  │  │  │  │  ├── Hiyori_m08.motion3.json
│  │  │  │  │  ├── Hiyori_m09.motion3.json
│  │  │  │  │  └── Hiyori_m10.motion3.json
│  │  │  │  ├── Hiyori.cdi3.json
│  │  │  │  ├── Hiyori.moc3
│  │  │  │  ├── Hiyori.model3.json
│  │  │  │  ├── Hiyori.physics3.json
│  │  │  │  ├── Hiyori.pose3.json
│  │  │  │  └── Hiyori.userdata3.json
│  │  │  ├── Mao
│  │  │  │  ├── expressions
│  │  │  │  │  ├── exp_01.exp3.json
│  │  │  │  │  ├── exp_02.exp3.json
│  │  │  │  │  ├── exp_03.exp3.json
│  │  │  │  │  ├── exp_04.exp3.json
│  │  │  │  │  ├── exp_05.exp3.json
│  │  │  │  │  ├── exp_06.exp3.json
│  │  │  │  │  ├── exp_07.exp3.json
│  │  │  │  │  └── exp_08.exp3.json
│  │  │  │  ├── Mao.2048
│  │  │  │  │  └── texture_00.png
│  │  │  │  ├── motions
│  │  │  │  │  ├── mtn_01.motion3.json
│  │  │  │  │  ├── mtn_02.motion3.json
│  │  │  │  │  ├── mtn_03.motion3.json
│  │  │  │  │  ├── mtn_04.motion3.json
│  │  │  │  │  ├── sample_01.motion3.json
│  │  │  │  │  ├── special_01.motion3.json
│  │  │  │  │  ├── special_02.motion3.json
│  │  │  │  │  └── special_03.motion3.json
│  │  │  │  ├── Mao.cdi3.json
│  │  │  │  ├── Mao.moc3
│  │  │  │  ├── Mao.model3.json
│  │  │  │  ├── Mao.physics3.json
│  │  │  │  └── Mao.pose3.json
│  │  │  ├── Mark
│  │  │  │  ├── Mark.2048
│  │  │  │  │  └── texture_00.png
│  │  │  │  ├── motions
│  │  │  │  │  ├── mark_m01.motion3.json
│  │  │  │  │  ├── mark_m02.motion3.json
│  │  │  │  │  ├── mark_m03.motion3.json
│  │  │  │  │  ├── mark_m04.motion3.json
│  │  │  │  │  ├── mark_m05.motion3.json
│  │  │  │  │  └── mark_m06.motion3.json
│  │  │  │  ├── Mark.cdi3.json
│  │  │  │  ├── Mark.moc3
│  │  │  │  ├── Mark.model3.json
│  │  │  │  ├── Mark.physics3.json
│  │  │  │  └── Mark.userdata3.json
│  │  │  ├── Natori
│  │  │  │  ├── exp
│  │  │  │  │  ├── Angry.exp3.json
│  │  │  │  │  ├── Blushing.exp3.json
│  │  │  │  │  ├── exp_01.exp3.json
│  │  │  │  │  ├── exp_02.exp3.json
│  │  │  │  │  ├── exp_03.exp3.json
│  │  │  │  │  ├── exp_04.exp3.json
│  │  │  │  │  ├── exp_05.exp3.json
│  │  │  │  │  ├── Normal.exp3.json
│  │  │  │  │  ├── Sad.exp3.json
│  │  │  │  │  ├── Smile.exp3.json
│  │  │  │  │  └── Surprised.exp3.json
│  │  │  │  ├── motions
│  │  │  │  │  ├── mtn_00.motion3.json
│  │  │  │  │  ├── mtn_01.motion3.json
│  │  │  │  │  ├── mtn_02.motion3.json
│  │  │  │  │  ├── mtn_03.motion3.json
│  │  │  │  │  ├── mtn_04.motion3.json
│  │  │  │  │  ├── mtn_05.motion3.json
│  │  │  │  │  ├── mtn_06.motion3.json
│  │  │  │  │  └── mtn_07.motion3.json
│  │  │  │  ├── Natori.2048
│  │  │  │  │  └── texture_00.png
│  │  │  │  ├── Natori.cdi3.json
│  │  │  │  ├── Natori.moc3
│  │  │  │  ├── Natori.model3.json
│  │  │  │  ├── Natori.physics3.json
│  │  │  │  └── Natori.pose3.json
│  │  │  ├── Rice
│  │  │  │  ├── motions
│  │  │  │  │  ├── idle.motion3.json
│  │  │  │  │  ├── mtn_01.motion3.json
│  │  │  │  │  ├── mtn_02.motion3.json
│  │  │  │  │  └── mtn_03.motion3.json
│  │  │  │  ├── Rice.2048
│  │  │  │  │  ├── texture_00.png
│  │  │  │  │  └── texture_01.png
│  │  │  │  ├── Rice.cdi3.json
│  │  │  │  ├── Rice.moc3
│  │  │  │  ├── Rice.model3.json
│  │  │  │  └── Rice.physics3.json
│  │  │  ├── Wanko
│  │  │  │  ├── motions
│  │  │  │  │  ├── idle_01.motion3.json
│  │  │  │  │  ├── idle_02.motion3.json
│  │  │  │  │  ├── idle_03.motion3.json
│  │  │  │  │  ├── idle_04.motion3.json
│  │  │  │  │  ├── shake_01.motion3.json
│  │  │  │  │  ├── shake_02.motion3.json
│  │  │  │  │  ├── touch_01.motion3.json
│  │  │  │  │  ├── touch_02.motion3.json
│  │  │  │  │  ├── touch_03.motion3.json
│  │  │  │  │  ├── touch_04.motion3.json
│  │  │  │  │  ├── touch_05.motion3.json
│  │  │  │  │  └── touch_06.motion3.json
│  │  │  │  ├── Wanko.1024
│  │  │  │  │  └── texture_00.png
│  │  │  │  ├── Wanko.cdi3.json
│  │  │  │  ├── Wanko.moc3
│  │  │  │  ├── Wanko.model3.json
│  │  │  │  └── Wanko.physics3.json
│  │  │  ├── back_class_normal.png
│  │  │  ├── close.png
│  │  │  └── icon_gear.png
│  │  └── Vulkan
│  │     ├── Demo
│  │     │  └── proj.win.cmake
│  │     │     ├── scripts
│  │     │     │  ├── nmake_msvc2019.bat
│  │     │     │  ├── nmake_msvc2022.bat
│  │     │     │  ├── proj_msvc2019.bat
│  │     │     │  ├── proj_msvc2022.bat
│  │     │     │  └── _msvc_common.bat
│  │     │     ├── src
│  │     │     │  ├── CMakeLists.txt
│  │     │     │  ├── LAppAllocator.cpp
│  │     │     │  ├── LAppAllocator.hpp
│  │     │     │  ├── LAppDefine.cpp
│  │     │     │  ├── LAppDefine.hpp
│  │     │     │  ├── LAppDelegate.cpp
│  │     │     │  ├── LAppDelegate.hpp
│  │     │     │  ├── LAppLive2DManager.cpp
│  │     │     │  ├── LAppLive2DManager.hpp
│  │     │     │  ├── LAppModel.cpp
│  │     │     │  ├── LAppModel.hpp
│  │     │     │  ├── LAppPal.cpp
│  │     │     │  ├── LAppPal.hpp
│  │     │     │  ├── LAppSprite.cpp
│  │     │     │  ├── LAppSprite.hpp
│  │     │     │  ├── LAppTextureManager.cpp
│  │     │     │  ├── LAppTextureManager.hpp
│  │     │     │  ├── LAppView.cpp
│  │     │     │  ├── LAppView.hpp
│  │     │     │  ├── LAppWavFileHandler.cpp
│  │     │     │  ├── LAppWavFileHandler.hpp
│  │     │     │  ├── main.cpp
│  │     │     │  ├── SwapchainManager.cpp
│  │     │     │  ├── SwapchainManager.hpp
│  │     │     │  ├── TouchManager.cpp
│  │     │     │  ├── TouchManager.hpp
│  │     │     │  ├── VulkanManager.cpp
│  │     │     │  └── VulkanManager.hpp
│  │     │     └── CMakeLists.txt
│  │     ├── Shaders
│  │     │  ├── src
│  │     │  │  ├── common.glsl
│  │     │  │  ├── FragSprite.frag
│  │     │  │  └── VertSprite.vert
│  │     │  └── CMakeLists.txt
│  │     ├── thirdParty
│  │     │  ├── scripts
│  │     │  │  ├── setup_glew_glfw
│  │     │  │  └── setup_glew_glfw.bat
│  │     │  └── stb
│  │     │     ├── README.md
│  │     │     └── stb_image.h
│  │     ├── README.ja.md
│  │     └── README.md
│  ├── CHANGELOG.md
│  ├── cubism-info.yml
│  ├── LICENSE.md
│  ├── logor.png
│  ├── logos.png
│  ├── NOTICE.ja.md
│  ├── NOTICE.md
│  ├── README.ja.md
│  └── README.md
├── gui
│  ├── game
│  │  ├── gui
│  │  │  ├── bubble.png
│  │  │  └── thoughtbubble.png
│  │  ├── gui.rpy
│  │  ├── guisupport.rpy
│  │  ├── options.rpy
│  │  ├── screens.rpy
│  │  ├── script.rpy
│  │  └── testcases.rpy
│  └── project.json
├── launcher
│  ├── game
│  │  ├── fonts
│  │  │  ├── Roboto-Light.ttf
│  │  │  └── Roboto-Regular.ttf
│  │  ├── gui7
│  │  │  ├── code.py
│  │  │  ├── icon.png
│  │  │  ├── images.py
│  │  │  ├── parameters.py
│  │  │  └── __init__.py
│  │  ├── images
│  │  │  ├── background.png
│  │  │  ├── logo.png
│  │  │  ├── logo32.png
│  │  │  ├── pattern.png
│  │  │  ├── window-icon-mac.png
│  │  │  ├── window-icon.png
│  │  │  └── window.png
│  │  ├── tl
│  │  │  ├── arabic
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpym
│  │  │  │  └── style.rpy
│  │  │  ├── danish
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpym
│  │  │  ├── finnish
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── style.rpy
│  │  │  ├── french
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpym
│  │  │  ├── german
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpym
│  │  │  ├── greek
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── style.rpy
│  │  │  │  ├── Z_changelog.txt
│  │  │  │  └── Z_ReadMe.txt
│  │  │  ├── indonesian
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpym
│  │  │  │  └── style.rpy
│  │  │  ├── italian
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpym
│  │  │  ├── japanese
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpym
│  │  │  │  └── style.rpy
│  │  │  ├── korean
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpym
│  │  │  │  └── style.rpy
│  │  │  ├── malay
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpym
│  │  │  │  └── style.rpy
│  │  │  ├── piglatin
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpym
│  │  │  ├── polish
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpym
│  │  │  ├── portuguese
│  │  │  │  ├── about.rpy
│  │  │  │  ├── add_file.rpy
│  │  │  │  ├── android.rpy
│  │  │  │  ├── choose_directory.rpy
│  │  │  │  ├── choose_theme.rpy
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── distribute.rpy
│  │  │  │  ├── distribute_gui.rpy
│  │  │  │  ├── editor.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── front_page.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── interface.rpy
│  │  │  │  ├── ios.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── navigation.rpy
│  │  │  │  ├── new_project.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── preferences.rpy
│  │  │  │  ├── project.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── style.rpy
│  │  │  │  ├── translations.rpy
│  │  │  │  └── updater.rpy
│  │  │  ├── russian
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpym
│  │  │  ├── schinese
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpym
│  │  │  │  └── style.rpy
│  │  │  ├── spanish
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── obsolete.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpym
│  │  │  ├── tchinese
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpym
│  │  │  │  └── style.rpy
│  │  │  ├── turkish
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpym
│  │  │  ├── ukrainian
│  │  │  │  ├── common.rpy
│  │  │  │  ├── developer.rpy
│  │  │  │  ├── error.rpy
│  │  │  │  ├── gui.rpy
│  │  │  │  ├── launcher.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpym
│  │  │  └── vietnamese
│  │  │     ├── common.rpy
│  │  │     ├── developer.rpy
│  │  │     ├── error.rpy
│  │  │     ├── gui.rpy
│  │  │     ├── launcher.rpy
│  │  │     ├── obsolete.rpy
│  │  │     ├── options.rpy
│  │  │     └── screens.rpy
│  │  ├── ability.rpy
│  │  ├── about.rpy
│  │  ├── add_file.rpy
│  │  ├── android.rpy
│  │  ├── androidstrings.rpy
│  │  ├── archiver.rpy
│  │  ├── change_icon.py
│  │  ├── choose_directory.rpy
│  │  ├── choose_theme.rpy
│  │  ├── consolecommand.rpy
│  │  ├── distribute.rpy
│  │  ├── distribute_gui.rpy
│  │  ├── dmgcheck.rpy
│  │  ├── download.rpy
│  │  ├── editor.rpy
│  │  ├── entitlements.plist
│  │  ├── front_page.rpy
│  │  ├── gui7.rpy
│  │  ├── install.rpy
│  │  ├── installer.py
│  │  ├── installer.rpy
│  │  ├── interface.rpy
│  │  ├── ios.rpy
│  │  ├── itch.rpy
│  │  ├── mac.rpy
│  │  ├── mobilebuild.rpy
│  │  ├── navigation.rpy
│  │  ├── new_project.rpy
│  │  ├── options.rpy
│  │  ├── package_formats.rpy
│  │  ├── preferences.rpy
│  │  ├── project.rpy
│  │  ├── renpy_ecdsa_public.pem
│  │  ├── renpy_public.pem
│  │  ├── style.rpy
│  │  ├── tail.rpy
│  │  ├── testcases.rpy
│  │  ├── theme_data.rpy
│  │  ├── translations.rpy
│  │  ├── updater.rpy
│  │  ├── util.rpy
│  │  ├── web.rpy
│  │  └── webserver.py
│  ├── skin
│  │  ├── skin.rpy
│  │  └── skin_background.jpg
│  ├── Atom.edit.py
│  ├── icon.icns
│  ├── None.edit.py
│  ├── project.json
│  ├── System Editor.edit.py
│  ├── Visual Studio Code (System).edit.py
│  └── Visual Studio Code.edit.py
├── live2d
│  ├── include
│  ├── lib
│  ├── models
│  └── src
├── module
│  ├── emoji
│  │  ├── emoji-test.txt
│  │  └── make_emoji_trie.py
│  ├── include
│  │  ├── freetype.pxd
│  │  ├── pygame.pxd
│  │  ├── pygame_sdl2.pxd
│  │  ├── sdl2.pxd
│  │  ├── style_common.pxi
│  │  └── ttgsubtable.pxd
│  ├── libhydrogen
│  │  ├── impl
│  │  │  ├── gimli-core
│  │  │  │  ├── portable.h
│  │  │  │  └── sse2.h
│  │  │  ├── random
│  │  │  │  ├── avr.h
│  │  │  │  ├── esp32.h
│  │  │  │  ├── linux_kernel.h
│  │  │  │  ├── mbed.h
│  │  │  │  ├── nrf52832.h
│  │  │  │  ├── particle.h
│  │  │  │  ├── riot.h
│  │  │  │  ├── rtthread.h
│  │  │  │  ├── stm32.h
│  │  │  │  ├── unix.h
│  │  │  │  ├── wasi.h
│  │  │  │  └── windows.h
│  │  │  ├── common.h
│  │  │  ├── core.h
│  │  │  ├── gimli-core.h
│  │  │  ├── hash.h
│  │  │  ├── hydrogen_p.h
│  │  │  ├── kdf.h
│  │  │  ├── kx.h
│  │  │  ├── pwhash.h
│  │  │  ├── random.h
│  │  │  ├── secretbox.h
│  │  │  ├── sign.h
│  │  │  └── x25519.h
│  │  ├── .gitignore
│  │  ├── hydrogen.c
│  │  ├── hydrogen.h
│  │  ├── LICENSE
│  │  └── Makefile
│  ├── tinyfiledialogs
│  │  ├── README.txt
│  │  ├── tinyfiledialogs.c
│  │  └── tinyfiledialogs.h
│  ├── uguu
│  │  ├── generate_required_functions.py
│  │  ├── gl.xml
│  │  ├── uguugl_pxd_header.pxd
│  │  ├── uguugl_pyx_header.pyx
│  │  ├── uguu_pyx_header.pyx
│  │  └── xml_to_pyx.py
│  ├── build.sh
│  ├── build_android.sh
│  ├── build_win32.sh
│  ├── core.c
│  ├── ffmedia.c
│  ├── ftsupport.c
│  ├── ftsupport.h
│  ├── generate_linebreak.py
│  ├── generate_styles.py
│  ├── IMG_savepng.c
│  ├── IMG_savepng.h
│  ├── LineBreak.txt
│  ├── pyfreetype.h
│  ├── renpy.h
│  ├── renpybidicore.c
│  ├── renpybidicore.h
│  ├── renpygl.h
│  ├── renpysound_core.c
│  ├── renpysound_core.h
│  ├── Setup
│  ├── setup.py
│  ├── Setup.tfd
│  ├── setuplib.py
│  ├── steamcallbacks.h
│  ├── symbolic_matrix.py
│  ├── ttgsubtable.c
│  ├── ttgsubtable.h
│  ├── _renpy.pyx
│  ├── _renpybidi.pyx
│  └── _renpytfd.pyx
├── renpy
│  ├── audio
│  │  ├── audio.py
│  │  ├── filter.pxd
│  │  ├── filter.pyx
│  │  ├── music.py
│  │  ├── renpysound.pyx
│  │  ├── sound.py
│  │  ├── webaudio.py
│  │  └── __init__.py
│  ├── common
│  │  ├── _compat
│  │  │  ├── gamemenu.rpym
│  │  │  ├── library.rpym
│  │  │  ├── mainmenu.rpym
│  │  │  ├── preferences.rpym
│  │  │  ├── styles.rpym
│  │  │  └── themes.rpym
│  │  ├── _developer
│  │  │  ├── developer.rpym
│  │  │  └── inspector.rpym
│  │  ├── _layout
│  │  │  ├── classic_joystick_preferences.rpym
│  │  │  ├── classic_load_save.rpym
│  │  │  ├── classic_main_menu.rpym
│  │  │  ├── classic_navigation.rpym
│  │  │  ├── classic_preferences.rpym
│  │  │  ├── classic_preferences_common.rpym
│  │  │  ├── classic_yesno_prompt.rpym
│  │  │  ├── grouped_main_menu.rpym
│  │  │  ├── grouped_navigation.rpym
│  │  │  ├── imagemap_common.rpym
│  │  │  ├── imagemap_load_save.rpym
│  │  │  ├── imagemap_main_menu.rpym
│  │  │  ├── imagemap_navigation.rpym
│  │  │  ├── imagemap_preferences.rpym
│  │  │  ├── imagemap_yesno_prompt.rpym
│  │  │  ├── one_column_preferences.rpym
│  │  │  ├── screen_joystick_preferences.rpym
│  │  │  ├── screen_load_save.rpym
│  │  │  ├── screen_main_menu.rpym
│  │  │  ├── screen_preferences.rpym
│  │  │  ├── screen_yesno_prompt.rpym
│  │  │  ├── scrolling_load_save.rpym
│  │  │  └── two_column_preferences.rpym
│  │  ├── _outline
│  │  │  ├── bar.png
│  │  │  ├── circle.png
│  │  │  └── vbar.png
│  │  ├── _placeholder
│  │  │  ├── boy.png
│  │  │  └── girl.png
│  │  ├── _roundrect
│  │  │  ├── rr12.png
│  │  │  ├── rr12g.png
│  │  │  ├── rr6.png
│  │  │  ├── rr6g.png
│  │  │  ├── rrscrollbar.png
│  │  │  ├── rrscrollbar_thumb.png
│  │  │  ├── rrslider_empty.png
│  │  │  ├── rrslider_full.png
│  │  │  ├── rrslider_thumb.png
│  │  │  ├── rrvscrollbar.png
│  │  │  ├── rrvscrollbar_thumb.png
│  │  │  ├── rrvslider_empty.png
│  │  │  ├── rrvslider_full.png
│  │  │  └── rrvslider_thumb.png
│  │  ├── _theme_amie2
│  │  │  ├── bar.png
│  │  │  ├── button.png
│  │  │  ├── button_hover.png
│  │  │  ├── frame.png
│  │  │  ├── hover_bar.png
│  │  │  └── hover_frame.png
│  │  ├── _theme_austen
│  │  │  ├── auscrollbar.png
│  │  │  ├── auscrollbar_thumb.png
│  │  │  ├── auslider_empty.png
│  │  │  ├── auslider_full.png
│  │  │  ├── auslider_thumb.png
│  │  │  ├── auvscrollbar.png
│  │  │  ├── auvscrollbar_thumb.png
│  │  │  ├── auvslider_empty.png
│  │  │  ├── auvslider_full.png
│  │  │  ├── auvslider_thumb.png
│  │  │  └── au_box.png
│  │  ├── _theme_awt
│  │  │  ├── bar_full.png
│  │  │  ├── bar_full_overlay.png
│  │  │  ├── bar_thumb.gif
│  │  │  ├── bar_thumb.png
│  │  │  ├── bar_thumb_overlay.png
│  │  │  ├── button.png
│  │  │  ├── button_disabled_overlay.png
│  │  │  ├── button_overlay.png
│  │  │  ├── button_overlay_highlight.png
│  │  │  ├── button_selected.png
│  │  │  ├── button_selected_overlay.png
│  │  │  ├── button_selected_overlay_highlight.png
│  │  │  ├── frame.png
│  │  │  ├── frame_overlay.png
│  │  │  ├── OFL.txt
│  │  │  ├── Quicksand-Bold.ttf
│  │  │  ├── Quicksand-Regular.ttf
│  │  │  ├── radio_base.png
│  │  │  ├── radio_base_overlay.png
│  │  │  ├── radio_selected_hover.png
│  │  │  ├── radio_unselected.png
│  │  │  ├── radio_unselected_hover.png
│  │  │  ├── scroller.png
│  │  │  ├── scroller_overlay.png
│  │  │  ├── slider_empty_all.png
│  │  │  ├── slider_empty_overlay.png
│  │  │  ├── slider_full.png
│  │  │  ├── slider_full_overlay.png
│  │  │  ├── vscroller.png
│  │  │  ├── vscroller_overlay.png
│  │  │  ├── vslider_empty_all.png
│  │  │  ├── vslider_full.png
│  │  │  ├── vslider_full_overlay.png
│  │  │  ├── vthumb.png
│  │  │  ├── vthumb_overlay.png
│  │  │  ├── v_bar_full.png
│  │  │  ├── v_bar_full_overlay.png
│  │  │  ├── v_bar_thumb.png
│  │  │  └── v_bar_thumb_overlay.png
│  │  ├── _theme_bordered
│  │  │  ├── brscrollbar.png
│  │  │  ├── brscrollbar_thumb.png
│  │  │  ├── brslider_empty.png
│  │  │  ├── brslider_full.png
│  │  │  ├── brslider_thumb.png
│  │  │  ├── brvscrollbar.png
│  │  │  ├── brvscrollbar_thumb.png
│  │  │  ├── brvslider_empty.png
│  │  │  ├── brvslider_full.png
│  │  │  ├── brvslider_thumb.png
│  │  │  └── br_box.png
│  │  ├── _theme_crayon
│  │  │  ├── cryscrollbar.png
│  │  │  ├── cryscrollbar_thumb.png
│  │  │  ├── cryslider_empty.png
│  │  │  ├── cryslider_full.png
│  │  │  ├── cryslider_thumb.png
│  │  │  ├── cryvscrollbar.png
│  │  │  ├── cryvscrollbar_thumb.png
│  │  │  ├── cryvslider_empty.png
│  │  │  ├── cryvslider_full.png
│  │  │  ├── cryvslider_thumb.png
│  │  │  ├── cry_box.png
│  │  │  ├── cry_box2.png
│  │  │  └── rr12g.png
│  │  ├── _theme_diamond
│  │  │  ├── dscrollbar.png
│  │  │  ├── dscrollbar_thumb.png
│  │  │  ├── dslider_empty.png
│  │  │  ├── dslider_full.png
│  │  │  ├── dslider_thumb.png
│  │  │  ├── dvscrollbar.png
│  │  │  ├── dvscrollbar_thumb.png
│  │  │  ├── dvslider_empty.png
│  │  │  ├── dvslider_full.png
│  │  │  ├── dvslider_thumb.png
│  │  │  └── d_box.png
│  │  ├── _theme_glow
│  │  │  ├── gscrollbar.png
│  │  │  ├── gscrollbar_thumb.png
│  │  │  ├── gslider_empty.png
│  │  │  ├── gslider_full.png
│  │  │  ├── gslider_thumb.png
│  │  │  ├── gvscrollbar.png
│  │  │  ├── gvscrollbar_thumb.png
│  │  │  ├── gvslider_empty.png
│  │  │  ├── gvslider_full.png
│  │  │  ├── gvslider_thumb.png
│  │  │  ├── g_box.png
│  │  │  └── g_outline.png
│  │  ├── _theme_marker
│  │  │  ├── inkscrollbar.png
│  │  │  ├── inkscrollbar_thumb.png
│  │  │  ├── inkslider_empty.png
│  │  │  ├── inkslider_full.png
│  │  │  ├── inkslider_thumb.png
│  │  │  ├── inkvscrollbar.png
│  │  │  ├── inkvscrollbar_thumb.png
│  │  │  ├── inkvslider_empty.png
│  │  │  ├── inkvslider_full.png
│  │  │  ├── inkvslider_thumb.png
│  │  │  └── ink_box.png
│  │  ├── _theme_regal
│  │  │  ├── rescrollbar.png
│  │  │  ├── rescrollbar_thumb.png
│  │  │  ├── reslider_empty.png
│  │  │  ├── reslider_full.png
│  │  │  ├── reslider_thumb.png
│  │  │  ├── revscrollbar.png
│  │  │  ├── revscrollbar_thumb.png
│  │  │  ├── revslider_empty.png
│  │  │  ├── revslider_full.png
│  │  │  ├── revslider_thumb.png
│  │  │  └── re_box.png
│  │  ├── _theme_threeD
│  │  │  ├── thscrollbar.png
│  │  │  ├── thscrollbar_thumb.png
│  │  │  ├── thslider_empty.png
│  │  │  ├── thslider_full.png
│  │  │  ├── thslider_thumb.png
│  │  │  ├── thvscrollbar.png
│  │  │  ├── thvscrollbar_thumb.png
│  │  │  ├── thvslider_empty.png
│  │  │  ├── thvslider_full.png
│  │  │  ├── thvslider_thumb.png
│  │  │  └── th_box.png
│  │  ├── _theme_tv
│  │  │  ├── tscrollbar.png
│  │  │  ├── tscrollbar_thumb.png
│  │  │  ├── tslider_empty.png
│  │  │  ├── tslider_full.png
│  │  │  ├── tslider_thumb.png
│  │  │  ├── tvscrollbar.png
│  │  │  ├── tvscrollbar_thumb.png
│  │  │  ├── tvslider_empty.png
│  │  │  ├── tvslider_full.png
│  │  │  ├── tvslider_thumb.png
│  │  │  └── t_box.png
│  │  ├── 000atl.rpy
│  │  ├── 000namespaces.rpy
│  │  ├── 000statements.rpy
│  │  ├── 000window.rpy
│  │  ├── 00accessibility.rpy
│  │  ├── 00achievement.rpy
│  │  ├── 00action_audio.rpy
│  │  ├── 00action_control.rpy
│  │  ├── 00action_data.rpy
│  │  ├── 00action_file.rpy
│  │  ├── 00action_menu.rpy
│  │  ├── 00action_other.rpy
│  │  ├── 00audio.rpy
│  │  ├── 00barvalues.rpy
│  │  ├── 00build.rpy
│  │  ├── 00compat.rpy
│  │  ├── 00console.rpy
│  │  ├── 00db_ren.py
│  │  ├── 00defaults.rpy
│  │  ├── 00definitions.rpy
│  │  ├── 00director.rpy
│  │  ├── 00gallery.rpy
│  │  ├── 00gamemenu.rpy
│  │  ├── 00gamepad.rpy
│  │  ├── 00gltest.rpy
│  │  ├── 00gui.rpy
│  │  ├── 00iap.rpy
│  │  ├── 00icon.rpy
│  │  ├── 00iconbutton.rpy
│  │  ├── 00images.rpy
│  │  ├── 00inputvalues.rpy
│  │  ├── 00keymap.rpy
│  │  ├── 00layeredimage.rpy
│  │  ├── 00layout.rpy
│  │  ├── 00library.rpy
│  │  ├── 00matrixcolor.rpy
│  │  ├── 00matrixtransform.rpy
│  │  ├── 00mixers.rpy
│  │  ├── 00mousedisplayable.rpy
│  │  ├── 00musicroom.rpy
│  │  ├── 00nvl_mode.rpy
│  │  ├── 00obsolete.rpy
│  │  ├── 00performance.rpy
│  │  ├── 00placeholder.rpy
│  │  ├── 00preferences.rpy
│  │  ├── 00shaders.rpy
│  │  ├── 00sideimage.rpy
│  │  ├── 00speechbubble.rpy
│  │  ├── 00splines.rpy
│  │  ├── 00sshtransition_ren.py
│  │  ├── 00start.rpy
│  │  ├── 00steam.rpy
│  │  ├── 00style.rpy
│  │  ├── 00stylepreferences.rpy
│  │  ├── 00sync.rpy
│  │  ├── 00textshader_ren.py
│  │  ├── 00themes.rpy
│  │  ├── 00touchkeyboard.rpy
│  │  ├── 00translation.rpy
│  │  ├── 00updater.rpy
│  │  ├── 00voice.rpy
│  │  ├── blindstile.png
│  │  ├── DejaVuSans-Bold.ttf
│  │  ├── DejaVuSans.ttf
│  │  ├── DejaVuSans.txt
│  │  ├── gamecontrollerdb.txt
│  │  ├── squarestile.png
│  │  ├── TwemojiCOLRv0.ttf
│  │  ├── TwemojiCOLRv0.txt
│  │  ├── _audio.js
│  │  ├── _audio_filter.js
│  │  ├── _dl_silence.ogg
│  │  ├── _errorhandling.rpym
│  │  ├── _missing_image.png
│  │  ├── _OpenDyslexic3-Regular.ttf
│  │  ├── _OpenDyslexic3-Regular.txt
│  │  ├── _shaders.rpym
│  │  ├── _silence.ogg
│  │  ├── _transparent_tile.png
│  │  └── _tv_unsafe.png
│  ├── compat
│  │  ├── fixes.py
│  │  ├── pickle.py
│  │  └── __init__.py
│  ├── display
│  │  ├── accelerator.pyx
│  │  ├── anim.py
│  │  ├── behavior.py
│  │  ├── controller.py
│  │  ├── core.py
│  │  ├── displayable.py
│  │  ├── dragdrop.py
│  │  ├── emulator.py
│  │  ├── error.py
│  │  ├── focus.py
│  │  ├── gesture.py
│  │  ├── im.py
│  │  ├── image.py
│  │  ├── imagelike.py
│  │  ├── imagemap.py
│  │  ├── joystick.py
│  │  ├── layout.py
│  │  ├── matrix.pxd
│  │  ├── matrix.pyx
│  │  ├── matrix_functions.pxi
│  │  ├── minigame.py
│  │  ├── model.py
│  │  ├── module.py
│  │  ├── motion.py
│  │  ├── movetransition.py
│  │  ├── particle.py
│  │  ├── pgrender.py
│  │  ├── predict.py
│  │  ├── presplash.py
│  │  ├── quaternion.pyx
│  │  ├── render.pxd
│  │  ├── render.pyx
│  │  ├── scale.py
│  │  ├── scenelists.py
│  │  ├── screen.py
│  │  ├── swdraw.py
│  │  ├── transform.py
│  │  ├── transition.py
│  │  ├── tts.py
│  │  ├── video.py
│  │  ├── viewport.py
│  │  └── __init__.py
│  ├── exports
│  │  ├── actionexports.py
│  │  ├── commonexports.py
│  │  ├── contextexports.py
│  │  ├── debugexports.py
│  │  ├── displayexports.py
│  │  ├── fetchexports.py
│  │  ├── inputexports.py
│  │  ├── loaderexports.py
│  │  ├── mediaexports.py
│  │  ├── menuexports.py
│  │  ├── persistentexports.py
│  │  ├── platformexports.py
│  │  ├── predictexports.py
│  │  ├── restartexports.py
│  │  ├── rollbackexports.py
│  │  ├── sayexports.py
│  │  ├── scriptexports.py
│  │  ├── statementexports.py
│  │  └── __init__.py
│  ├── gl2
│  │  ├── gl2debug.py
│  │  ├── gl2draw.pxd
│  │  ├── gl2draw.pyx
│  │  ├── gl2functions.py
│  │  ├── gl2mesh.pxd
│  │  ├── gl2mesh.pyx
│  │  ├── gl2mesh2.pxd
│  │  ├── gl2mesh2.pyx
│  │  ├── gl2mesh3.pxd
│  │  ├── gl2mesh3.pyx
│  │  ├── gl2model.pxd
│  │  ├── gl2model.pyx
│  │  ├── gl2polygon.pxd
│  │  ├── gl2polygon.pyx
│  │  ├── gl2shader.pxd
│  │  ├── gl2shader.pyx
│  │  ├── gl2shadercache.py
│  │  ├── gl2texture.pxd
│  │  ├── gl2texture.pyx
│  │  ├── live2d.py
│  │  ├── live2dcsm.pxi
│  │  ├── live2dmodel.pyx
│  │  ├── live2dmotion.py
│  │  └── __init__.py
│  ├── live2d
│  ├── sl2
│  │  ├── slast.py
│  │  ├── sldisplayables.py
│  │  ├── slparser.py
│  │  ├── slproperties.py
│  │  └── __init__.py
│  ├── styledata
│  │  ├── styleclass.pyx
│  │  ├── stylesets.pyx
│  │  ├── styleutil.py
│  │  └── __init__.py
│  ├── test
│  │  ├── testast.py
│  │  ├── testexecution.py
│  │  ├── testfocus.py
│  │  ├── testkey.py
│  │  ├── testmouse.py
│  │  ├── testparser.py
│  │  └── __init__.py
│  ├── text
│  │  ├── emoji_trie.py
│  │  ├── extras.py
│  │  ├── font.py
│  │  ├── ftfont.pyx
│  │  ├── hbfont.pyx
│  │  ├── linebreak.pxi
│  │  ├── shader.py
│  │  ├── text.py
│  │  ├── textsupport.pxd
│  │  ├── textsupport.pyx
│  │  ├── texwrap.pyx
│  │  └── __init__.py
│  ├── translation
│  │  ├── dialogue.py
│  │  ├── extract.py
│  │  ├── generation.py
│  │  ├── merge.py
│  │  ├── scanstrings.py
│  │  └── __init__.py
│  ├── uguu
│  │  ├── gl.pxd
│  │  ├── gl.pyx
│  │  ├── uguu.pyx
│  │  └── __init__.py
│  ├── update
│  │  ├── common.py
│  │  ├── download.py
│  │  ├── generate.py
│  │  ├── update.py
│  │  └── __init__.py
│  ├── add_from.py
│  ├── arguments.py
│  ├── ast.py
│  ├── atl.py
│  ├── bootstrap.py
│  ├── character.py
│  ├── color.py
│  ├── config.py
│  ├── curry.py
│  ├── debug.py
│  ├── defaultstore.py
│  ├── dump.py
│  ├── easy.py
│  ├── editor.py
│  ├── encryption.pyx
│  ├── error.py
│  ├── execution.py
│  ├── game.py
│  ├── lexer.py
│  ├── lexersupport.pyx
│  ├── lint.py
│  ├── loader.py
│  ├── loadsave.py
│  ├── log.py
│  ├── main.py
│  ├── memory.py
│  ├── minstore.py
│  ├── object.py
│  ├── parameter.py
│  ├── parser.py
│  ├── performance.py
│  ├── persistent.py
│  ├── preferences.py
│  ├── pyanalysis.py
│  ├── pydict.pyx
│  ├── python.py
│  ├── revertable.py
│  ├── rollback.py
│  ├── savelocation.py
│  ├── savetoken.py
│  ├── screenlang.py
│  ├── script.py
│  ├── scriptedit.py
│  ├── statements.py
│  ├── style.pxd
│  ├── style.pyx
│  ├── substitutions.py
│  ├── ui.py
│  ├── util.py
│  ├── versions.py
│  ├── warp.py
│  ├── webloader.py
│  └── __init__.py
├── scripts
│  ├── mac
│  │  ├── .gitignore
│  │  ├── entitlements.plist
│  │  ├── mac_dmg_client.sh
│  │  ├── mac_dmg_server.sh
│  │  ├── mac_sign_client.sh
│  │  ├── mac_sign_server.sh
│  │  └── wait_notarization.py
│  ├── pyi
│  │  └── android
│  │     └── apk.py
│  ├── rt
│  │  ├── augustina.rpy
│  │  ├── augustina_base.png
│  │  ├── augustina_eyebrows_normal.png
│  │  ├── augustina_eyebrows_oneup.png
│  │  ├── augustina_eyes_open.png
│  │  ├── augustina_eyes_wink.png
│  │  ├── augustina_glasses.png
│  │  ├── augustina_glasses_evil.png
│  │  ├── augustina_mouth_happy.png
│  │  ├── augustina_mouth_smile.png
│  │  ├── augustina_outfit_dress.png
│  │  ├── augustina_outfit_jeans.png
│  │  └── script.rpy
│  ├── add_all.sh
│  ├── alter_translations.py
│  ├── automatic_translate.py
│  ├── checksums.py
│  ├── check_copyright.py
│  ├── distribute_all.sh
│  ├── find_recursive_inner_functions.py
│  ├── fix_translations.py
│  ├── generate_pyi.py
│  ├── generate_update_keys.py
│  ├── itch_upload.sh
│  ├── merge_to_master.sh
│  ├── README.rst
│  ├── relative_imports.py
│  ├── release_changes.py
│  ├── rt.py
│  ├── sign_update.py
│  ├── sync.sh
│  ├── translate_launcher.sh
│  ├── update_compat_import.py
│  ├── update_copyright.py
│  ├── update_installer.py
│  ├── update_piglatin.sh
│  └── utflf.py
├── sdk-fonts
│  └── SourceHanSansLite.ttf
├── sphinx
│  ├── game
│  │  ├── doc.py
│  │  ├── renpy_json.py
│  │  ├── script.rpy
│  │  └── shaderdoc.py
│  ├── source
│  │  ├── gui
│  │  │  ├── bar.jpg
│  │  │  ├── borders1.png
│  │  │  ├── borders2.png
│  │  │  ├── borders3.png
│  │  │  ├── button_preferences.jpg
│  │  │  ├── easy_choice_screen.jpg
│  │  │  ├── easy_game_menu.jpg
│  │  │  ├── easy_main_menu.jpg
│  │  │  ├── easy_say_screen.jpg
│  │  │  ├── frame_confirm.jpg
│  │  │  ├── history.png
│  │  │  ├── intermediate_dialogue.jpg
│  │  │  ├── ivory-off-white-paper-texture.jpg
│  │  │  ├── namebox.jpg
│  │  │  ├── nvl.jpg
│  │  │  ├── overlay_game_menu.jpg
│  │  │  ├── overlay_main_menu.jpg
│  │  │  ├── scrollbar_history.jpg
│  │  │  ├── skip_notify.jpg
│  │  │  ├── slider_preferences.jpg
│  │  │  ├── slot_save.jpg
│  │  │  └── text.jpg
│  │  ├── oshs
│  │  │  └── game
│  │  │     ├── gui
│  │  │     │  ├── bar
│  │  │     │  │  ├── bottom.png
│  │  │     │  │  ├── left.png
│  │  │     │  │  ├── right.png
│  │  │     │  │  └── top.png
│  │  │     │  ├── button
│  │  │     │  │  ├── check_foreground.png
│  │  │     │  │  ├── check_selected_foreground.png
│  │  │     │  │  ├── choice_hover_background.png
│  │  │     │  │  ├── choice_idle_background.png
│  │  │     │  │  ├── hover_background.png
│  │  │     │  │  ├── idle_background.png
│  │  │     │  │  ├── quick_hover_background.png
│  │  │     │  │  ├── quick_idle_background.png
│  │  │     │  │  ├── radio_foreground.png
│  │  │     │  │  ├── radio_selected_foreground.png
│  │  │     │  │  ├── slot_hover_background.png
│  │  │     │  │  └── slot_idle_background.png
│  │  │     │  ├── overlay
│  │  │     │  │  ├── confirm.png
│  │  │     │  │  ├── game_menu.png
│  │  │     │  │  └── main_menu.png
│  │  │     │  ├── phone
│  │  │     │  │  ├── overlay
│  │  │     │  │  │  ├── game_menu.png
│  │  │     │  │  │  └── main_menu.png
│  │  │     │  │  ├── nvl.png
│  │  │     │  │  └── textbox.png
│  │  │     │  ├── scrollbar
│  │  │     │  │  ├── horizontal_hover_bar.png
│  │  │     │  │  ├── horizontal_hover_thumb.png
│  │  │     │  │  ├── horizontal_idle_bar.png
│  │  │     │  │  ├── horizontal_idle_thumb.png
│  │  │     │  │  ├── vertical_hover_bar.png
│  │  │     │  │  ├── vertical_hover_thumb.png
│  │  │     │  │  ├── vertical_idle_bar.png
│  │  │     │  │  └── vertical_idle_thumb.png
│  │  │     │  ├── slider
│  │  │     │  │  ├── horizontal_hover_bar.png
│  │  │     │  │  ├── horizontal_hover_thumb.png
│  │  │     │  │  ├── horizontal_idle_bar.png
│  │  │     │  │  ├── horizontal_idle_thumb.png
│  │  │     │  │  ├── vertical_hover_bar.png
│  │  │     │  │  ├── vertical_hover_thumb.png
│  │  │     │  │  ├── vertical_idle_bar.png
│  │  │     │  │  └── vertical_idle_thumb.png
│  │  │     │  ├── frame.png
│  │  │     │  ├── game_menu.png
│  │  │     │  ├── main_menu.png
│  │  │     │  ├── namebox.png
│  │  │     │  ├── notify.png
│  │  │     │  ├── nvl.png
│  │  │     │  ├── skip.png
│  │  │     │  ├── textbox.png
│  │  │     │  └── window_icon.png
│  │  │     ├── images
│  │  │     │  ├── borders.png
│  │  │     │  └── eileen happy.png
│  │  │     ├── ArchitectsDaughter.ttf
│  │  │     ├── gui.rpy
│  │  │     ├── OFL.txt
│  │  │     ├── options.rpy
│  │  │     ├── sample_audio.opus
│  │  │     ├── screens.rpy
│  │  │     └── script.rpy
│  │  ├── presplash
│  │  │  ├── presplash_background_1.png
│  │  │  ├── presplash_background_2.png
│  │  │  ├── presplash_foreground_1.png
│  │  │  └── presplash_foreground_2.png
│  │  ├── quickstart
│  │  │  ├── color.png
│  │  │  ├── launcher.png
│  │  │  ├── project_name.png
│  │  │  └── resolution.png
│  │  ├── _static
│  │  │  ├── custom.css
│  │  │  └── environment.txt
│  │  ├── _templates
│  │  │  └── layout.html
│  │  ├── 3dstage.rst
│  │  ├── achievement.rst
│  │  ├── android.rst
│  │  ├── atl.rst
│  │  ├── audio.rst
│  │  ├── audio_filters.rst
│  │  ├── axes_3d_1.png
│  │  ├── axes_3d_2.png
│  │  ├── axes_3d_3.png
│  │  ├── bubble.rst
│  │  ├── build.rst
│  │  ├── cdd.rst
│  │  ├── cds.rst
│  │  ├── changelog.rst
│  │  ├── changelog6.rst
│  │  ├── character_callbacks.rst
│  │  ├── chromeos.rst
│  │  ├── cli.rst
│  │  ├── color_class.rst
│  │  ├── commandline.jpg
│  │  ├── conditional.rst
│  │  ├── conf.py
│  │  ├── config.rst
│  │  ├── credits.rst
│  │  ├── custom_text_tags.rst
│  │  ├── developer_tools.rst
│  │  ├── dialogue.rst
│  │  ├── director.rst
│  │  ├── displayables.rst
│  │  ├── displaying_images.rst
│  │  ├── display_problems.rst
│  │  ├── docutils.conf
│  │  ├── downloader.rst
│  │  ├── drag_drop.rst
│  │  ├── editor.rst
│  │  ├── environment_variables.rst
│  │  ├── fetch.rst
│  │  ├── file_python.rst
│  │  ├── fill-translator-credits.py
│  │  ├── frame_example.png
│  │  ├── gesture.rst
│  │  ├── gui.rst
│  │  ├── gui_advanced.rst
│  │  ├── history.rst
│  │  ├── iap.rst
│  │  ├── im.rst
│  │  ├── incompatible.rst
│  │  ├── index.rst
│  │  ├── input.rst
│  │  ├── ios.rst
│  │  ├── keymap.rst
│  │  ├── keywords.py
│  │  ├── label.rst
│  │  ├── language_basics.rst
│  │  ├── launcher.rst
│  │  ├── layeredimage.rst
│  │  ├── license.rst
│  │  ├── lifecycle.rst
│  │  ├── live2d.rst
│  │  ├── logo.png
│  │  ├── matrix.rst
│  │  ├── matrixcolor.rst
│  │  ├── menus.rst
│  │  ├── model.rst
│  │  ├── mouse.rst
│  │  ├── movie.rst
│  │  ├── multiple.rst
│  │  ├── namespaces.rst
│  │  ├── navbar-logo.png
│  │  ├── nvl_mode.rst
│  │  ├── other.rst
│  │  ├── persistent.rst
│  │  ├── preferences.rst
│  │  ├── problems.rst
│  │  ├── python.rst
│  │  ├── quickstart.rst
│  │  ├── raspi.rst
│  │  ├── renpydoc.py
│  │  ├── ren_py.rst
│  │  ├── reserved.rst
│  │  ├── rooms.rst
│  │  ├── save_load_rollback.rst
│  │  ├── screens.rst
│  │  ├── screenshot.rst
│  │  ├── screen_actions.rst
│  │  ├── screen_optimization.rst
│  │  ├── screen_python.rst
│  │  ├── screen_special.rst
│  │  ├── security.rst
│  │  ├── self_voicing.rst
│  │  ├── shader_parts.rst
│  │  ├── side_image.rst
│  │  ├── skins.rst
│  │  ├── splashscreen_presplash.rst
│  │  ├── sponsors.html
│  │  ├── sponsors.rst
│  │  ├── sprites.rst
│  │  ├── statement_equivalents.rst
│  │  ├── store_variables.rst
│  │  ├── style.rst
│  │  ├── style_properties.rst
│  │  ├── template_projects.rst
│  │  ├── text.rst
│  │  ├── textshaders.rst
│  │  ├── thequestion.txt
│  │  ├── thequestion_nvl.rst
│  │  ├── transforms.rst
│  │  ├── transform_properties.rst
│  │  ├── transitions.rst
│  │  ├── translating_renpy.rst
│  │  ├── translation.rst
│  │  ├── trans_trans_python.rst
│  │  ├── updater.rst
│  │  ├── voice.rst
│  │  └── web.rst
│  ├── .gitignore
│  ├── build.sh
│  ├── checks.py
│  ├── Makefile
│  ├── upload.sh
│  └── upload_dev.sh
├── testcases
│  └── game
│     ├── sound
│     │  ├── 1.ogg
│     │  ├── 2.ogg
│     │  ├── 3.ogg
│     │  ├── 4.ogg
│     │  └── 5.ogg
│     ├── arrow.png
│     ├── eileen_concerned.png
│     ├── eileen_happy.png
│     ├── eileen_vhappy.png
│     ├── mygallery.rpy
│     ├── options.rpy
│     ├── screens.rpy
│     ├── script.rpy
│     └── test_musicroom.rpy
├── the_question
│  ├── game
│  │  ├── gui
│  │  │  ├── bar
│  │  │  │  ├── bottom.png
│  │  │  │  ├── left.png
│  │  │  │  ├── right.png
│  │  │  │  └── top.png
│  │  │  ├── button
│  │  │  │  ├── check_foreground.png
│  │  │  │  ├── check_selected_foreground.png
│  │  │  │  ├── choice_hover_background.png
│  │  │  │  ├── choice_idle_background.png
│  │  │  │  ├── hover_background.png
│  │  │  │  ├── idle_background.png
│  │  │  │  ├── quick_hover_background.png
│  │  │  │  ├── quick_idle_background.png
│  │  │  │  ├── radio_foreground.png
│  │  │  │  ├── radio_selected_foreground.png
│  │  │  │  ├── slot_hover_background.png
│  │  │  │  └── slot_idle_background.png
│  │  │  ├── overlay
│  │  │  │  ├── confirm.png
│  │  │  │  ├── game_menu.png
│  │  │  │  └── main_menu.png
│  │  │  ├── phone
│  │  │  │  ├── overlay
│  │  │  │  │  ├── game_menu.png
│  │  │  │  │  └── main_menu.png
│  │  │  │  ├── nvl.png
│  │  │  │  └── textbox.png
│  │  │  ├── scrollbar
│  │  │  │  ├── horizontal_hover_bar.png
│  │  │  │  ├── horizontal_hover_thumb.png
│  │  │  │  ├── horizontal_idle_bar.png
│  │  │  │  ├── horizontal_idle_thumb.png
│  │  │  │  ├── vertical_hover_bar.png
│  │  │  │  ├── vertical_hover_thumb.png
│  │  │  │  ├── vertical_idle_bar.png
│  │  │  │  └── vertical_idle_thumb.png
│  │  │  ├── slider
│  │  │  │  ├── horizontal_hover_bar.png
│  │  │  │  ├── horizontal_hover_thumb.png
│  │  │  │  ├── horizontal_idle_bar.png
│  │  │  │  ├── horizontal_idle_thumb.png
│  │  │  │  ├── vertical_hover_bar.png
│  │  │  │  ├── vertical_hover_thumb.png
│  │  │  │  ├── vertical_idle_bar.png
│  │  │  │  └── vertical_idle_thumb.png
│  │  │  ├── frame.png
│  │  │  ├── game_menu.png
│  │  │  ├── main_menu.png
│  │  │  ├── namebox.png
│  │  │  ├── notify.png
│  │  │  ├── nvl.png
│  │  │  ├── skip.png
│  │  │  ├── textbox.png
│  │  │  └── window_icon.png
│  │  ├── images
│  │  │  ├── bg club.jpg
│  │  │  ├── bg lecturehall.jpg
│  │  │  ├── bg meadow.jpg
│  │  │  ├── bg uni.jpg
│  │  │  ├── sylvie blue giggle.png
│  │  │  ├── sylvie blue normal.png
│  │  │  ├── sylvie blue smile.png
│  │  │  ├── sylvie blue surprised.png
│  │  │  ├── sylvie green giggle.png
│  │  │  ├── sylvie green normal.png
│  │  │  ├── sylvie green smile.png
│  │  │  └── sylvie green surprised.png
│  │  ├── tl
│  │  │  ├── czech
│  │  │  │  ├── common.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  ├── danish
│  │  │  │  ├── common.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  ├── french
│  │  │  │  ├── common.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  ├── italian
│  │  │  │  ├── common.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  ├── japanese
│  │  │  │  ├── common.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  ├── korean
│  │  │  │  ├── common.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  ├── malay
│  │  │  │  ├── common.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  ├── None
│  │  │  │  └── common.rpym
│  │  │  ├── russian
│  │  │  │  ├── common.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  ├── schinese
│  │  │  │  ├── common.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  ├── spanish
│  │  │  │  ├── common.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  ├── tchinese
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  └── script.rpy
│  │  │  └── ukrainian
│  │  │     ├── common.rpy
│  │  │     ├── options.rpy
│  │  │     ├── screens.rpy
│  │  │     └── script.rpy
│  │  ├── gui.rpy
│  │  ├── illurock.opus
│  │  ├── options.rpy
│  │  ├── screens.rpy
│  │  └── script.rpy
│  ├── android-icon_background.png
│  ├── android-icon_foreground.png
│  ├── android.json
│  ├── icon.icns
│  ├── icon.ico
│  ├── ios-icon.png
│  ├── ios-launchimage.png
│  ├── progressive_download.txt
│  └── project.json
├── tutorial
│  ├── game
│  │  ├── gui
│  │  │  ├── bar
│  │  │  │  ├── bottom.png
│  │  │  │  ├── left.png
│  │  │  │  ├── right.png
│  │  │  │  └── top.png
│  │  │  ├── button
│  │  │  │  ├── check_foreground.png
│  │  │  │  ├── check_selected_foreground.png
│  │  │  │  ├── choice_hover_background.png
│  │  │  │  ├── choice_idle_background.png
│  │  │  │  ├── hover_background.png
│  │  │  │  ├── idle_background.png
│  │  │  │  ├── quick_hover_background.png
│  │  │  │  ├── quick_idle_background.png
│  │  │  │  ├── radio_foreground.png
│  │  │  │  ├── radio_selected_foreground.png
│  │  │  │  ├── slot_hover_background.png
│  │  │  │  └── slot_idle_background.png
│  │  │  ├── overlay
│  │  │  │  ├── confirm.png
│  │  │  │  ├── game_menu.png
│  │  │  │  └── main_menu.png
│  │  │  ├── phone
│  │  │  │  ├── overlay
│  │  │  │  │  ├── game_menu.png
│  │  │  │  │  └── main_menu.png
│  │  │  │  ├── nvl.png
│  │  │  │  └── textbox.png
│  │  │  ├── scrollbar
│  │  │  │  ├── horizontal_hover_bar.png
│  │  │  │  ├── horizontal_hover_thumb.png
│  │  │  │  ├── horizontal_idle_bar.png
│  │  │  │  ├── horizontal_idle_thumb.png
│  │  │  │  ├── vertical_hover_bar.png
│  │  │  │  ├── vertical_hover_thumb.png
│  │  │  │  ├── vertical_idle_bar.png
│  │  │  │  └── vertical_idle_thumb.png
│  │  │  ├── slider
│  │  │  │  ├── horizontal_hover_bar.png
│  │  │  │  ├── horizontal_hover_thumb.png
│  │  │  │  ├── horizontal_idle_bar.png
│  │  │  │  ├── horizontal_idle_thumb.png
│  │  │  │  ├── vertical_hover_bar.png
│  │  │  │  ├── vertical_hover_thumb.png
│  │  │  │  ├── vertical_idle_bar.png
│  │  │  │  └── vertical_idle_thumb.png
│  │  │  ├── frame.png
│  │  │  ├── main_menu.jpg
│  │  │  ├── mouse0.png
│  │  │  ├── mouse1.png
│  │  │  ├── mouse2.png
│  │  │  ├── namebox.png
│  │  │  ├── notify.png
│  │  │  ├── nvl.png
│  │  │  ├── skip.png
│  │  │  ├── startextbox.png
│  │  │  ├── textbox.png
│  │  │  └── window_icon.png
│  │  ├── images
│  │  │  ├── bar empty hover.png
│  │  │  ├── bar empty idle.png
│  │  │  ├── bar full hover.png
│  │  │  ├── bar full idle.png
│  │  │  ├── bar thumb hover.png
│  │  │  ├── bar thumb idle.png
│  │  │  ├── bg cave.jpg
│  │  │  ├── bg panorama.webp
│  │  │  ├── bg pong field.png
│  │  │  ├── bg washington.jpg
│  │  │  ├── bg whitehouse.jpg
│  │  │  ├── button glossy hover.png
│  │  │  ├── button glossy idle.png
│  │  │  ├── check_foreground.png
│  │  │  ├── check_selected_foreground.png
│  │  │  ├── concert1.png
│  │  │  ├── concert2.png
│  │  │  ├── concert3.png
│  │  │  ├── eileen concerned.png
│  │  │  ├── eileen happy.png
│  │  │  ├── eileen vhappy.png
│  │  │  ├── hover_background.png
│  │  │  ├── idle_background.png
│  │  │  ├── imagedissolve circleiris.png
│  │  │  ├── imagedissolve circlewipe.png
│  │  │  ├── imagedissolve dream.png
│  │  │  ├── imagedissolve teleport.png
│  │  │  ├── imagemap ground.png
│  │  │  ├── imagemap hover.png
│  │  │  ├── imagemap volume hover.png
│  │  │  ├── imagemap volume idle.png
│  │  │  ├── imagemap volume insensitive.png
│  │  │  ├── imagemap volume selected_hover.png
│  │  │  ├── imagemap volume selected_idle.png
│  │  │  ├── launcher distribute.png
│  │  │  ├── launcher step1.webp
│  │  │  ├── launcher step2.webp
│  │  │  ├── launcher step3.webp
│  │  │  ├── launcher step4.webp
│  │  │  ├── launcher step5.webp
│  │  │  ├── launcher translate.png
│  │  │  ├── logo base.png
│  │  │  ├── logo bw.png
│  │  │  ├── logo solid.png
│  │  │  ├── lucy happy.png
│  │  │  ├── lucy mad.png
│  │  │  ├── magic.png
│  │  │  ├── ninepatch paper.png
│  │  │  ├── ninepatch.png
│  │  │  ├── popup hrpprefs.png
│  │  │  ├── popup prefs.png
│  │  │  ├── popup save.png
│  │  │  └── spotlight.png
│  │  ├── tl
│  │  │  ├── french
│  │  │  │  ├── 01example.rpy
│  │  │  │  ├── common.rpy
│  │  │  │  ├── indepth_character.rpy
│  │  │  │  ├── indepth_displayables.rpy
│  │  │  │  ├── indepth_minigame.rpy
│  │  │  │  ├── indepth_style.rpy
│  │  │  │  ├── indepth_text.rpy
│  │  │  │  ├── indepth_transitions.rpy
│  │  │  │  ├── indepth_translations.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpy
│  │  │  │  ├── tutorial_atl.rpy
│  │  │  │  ├── tutorial_director.rpy
│  │  │  │  ├── tutorial_distribute.rpy
│  │  │  │  ├── tutorial_nvlmode.rpy
│  │  │  │  ├── tutorial_playing.rpy
│  │  │  │  ├── tutorial_quickstart.rpy
│  │  │  │  ├── tutorial_screens.rpy
│  │  │  │  ├── tutorial_screen_displayables.rpy
│  │  │  │  └── tutorial_video.rpy
│  │  │  ├── japanese
│  │  │  │  ├── 01example.rpy
│  │  │  │  ├── common.rpy
│  │  │  │  ├── indepth_character.rpy
│  │  │  │  ├── indepth_displayables.rpy
│  │  │  │  ├── indepth_minigame.rpy
│  │  │  │  ├── indepth_style.rpy
│  │  │  │  ├── indepth_text.rpy
│  │  │  │  ├── indepth_transitions.rpy
│  │  │  │  ├── indepth_translations.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpy
│  │  │  │  ├── style.rpy
│  │  │  │  ├── tutorial_atl.rpy
│  │  │  │  ├── tutorial_director.rpy
│  │  │  │  ├── tutorial_distribute.rpy
│  │  │  │  ├── tutorial_nvlmode.rpy
│  │  │  │  ├── tutorial_playing.rpy
│  │  │  │  ├── tutorial_quickstart.rpy
│  │  │  │  ├── tutorial_screens.rpy
│  │  │  │  ├── tutorial_screen_displayables.rpy
│  │  │  │  └── tutorial_video.rpy
│  │  │  ├── korean
│  │  │  │  ├── 01example.rpy
│  │  │  │  ├── common.rpy
│  │  │  │  ├── indepth_character.rpy
│  │  │  │  ├── indepth_displayables.rpy
│  │  │  │  ├── indepth_minigame.rpy
│  │  │  │  ├── indepth_style.rpy
│  │  │  │  ├── indepth_text.rpy
│  │  │  │  ├── indepth_transitions.rpy
│  │  │  │  ├── indepth_translations.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpy
│  │  │  │  ├── tutorial_atl.rpy
│  │  │  │  ├── tutorial_director.rpy
│  │  │  │  ├── tutorial_distribute.rpy
│  │  │  │  ├── tutorial_nvlmode.rpy
│  │  │  │  ├── tutorial_playing.rpy
│  │  │  │  ├── tutorial_quickstart.rpy
│  │  │  │  ├── tutorial_screens.rpy
│  │  │  │  ├── tutorial_screen_displayables.rpy
│  │  │  │  └── tutorial_video.rpy
│  │  │  ├── None
│  │  │  │  └── common.rpym
│  │  │  ├── piglatin
│  │  │  │  ├── 01example.rpy
│  │  │  │  ├── common.rpy
│  │  │  │  ├── indepth_character.rpy
│  │  │  │  ├── indepth_displayables.rpy
│  │  │  │  ├── indepth_minigame.rpy
│  │  │  │  ├── indepth_style.rpy
│  │  │  │  ├── indepth_text.rpy
│  │  │  │  ├── indepth_transitions.rpy
│  │  │  │  ├── indepth_translations.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpy
│  │  │  │  ├── tutorial_atl.rpy
│  │  │  │  ├── tutorial_director.rpy
│  │  │  │  ├── tutorial_distribute.rpy
│  │  │  │  ├── tutorial_nvlmode.rpy
│  │  │  │  ├── tutorial_playing.rpy
│  │  │  │  ├── tutorial_quickstart.rpy
│  │  │  │  ├── tutorial_screens.rpy
│  │  │  │  ├── tutorial_screen_displayables.rpy
│  │  │  │  └── tutorial_video.rpy
│  │  │  ├── russian
│  │  │  │  ├── 01example.rpy
│  │  │  │  ├── common.rpy
│  │  │  │  ├── indepth_character.rpy
│  │  │  │  ├── indepth_displayables.rpy
│  │  │  │  ├── indepth_minigame.rpy
│  │  │  │  ├── indepth_style.rpy
│  │  │  │  ├── indepth_text.rpy
│  │  │  │  ├── indepth_transitions.rpy
│  │  │  │  ├── indepth_translations.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpy
│  │  │  │  ├── tutorial_atl.rpy
│  │  │  │  ├── tutorial_director.rpy
│  │  │  │  ├── tutorial_distribute.rpy
│  │  │  │  ├── tutorial_nvlmode.rpy
│  │  │  │  ├── tutorial_playing.rpy
│  │  │  │  ├── tutorial_quickstart.rpy
│  │  │  │  ├── tutorial_screens.rpy
│  │  │  │  ├── tutorial_screen_displayables.rpy
│  │  │  │  └── tutorial_video.rpy
│  │  │  ├── schinese
│  │  │  │  ├── 01example.rpy
│  │  │  │  ├── common.rpy
│  │  │  │  ├── indepth_character.rpy
│  │  │  │  ├── indepth_displayables.rpy
│  │  │  │  ├── indepth_minigame.rpy
│  │  │  │  ├── indepth_style.rpy
│  │  │  │  ├── indepth_text.rpy
│  │  │  │  ├── indepth_transitions.rpy
│  │  │  │  ├── indepth_translations.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpy
│  │  │  │  ├── style.rpy
│  │  │  │  ├── tutorial_atl.rpy
│  │  │  │  ├── tutorial_director.rpy
│  │  │  │  ├── tutorial_distribute.rpy
│  │  │  │  ├── tutorial_nvlmode.rpy
│  │  │  │  ├── tutorial_playing.rpy
│  │  │  │  ├── tutorial_quickstart.rpy
│  │  │  │  ├── tutorial_screens.rpy
│  │  │  │  ├── tutorial_screen_displayables.rpy
│  │  │  │  └── tutorial_video.rpy
│  │  │  ├── spanish
│  │  │  │  ├── 01example.rpy
│  │  │  │  ├── common.rpy
│  │  │  │  ├── indepth_character.rpy
│  │  │  │  ├── indepth_displayables.rpy
│  │  │  │  ├── indepth_minigame.rpy
│  │  │  │  ├── indepth_style.rpy
│  │  │  │  ├── indepth_text.rpy
│  │  │  │  ├── indepth_transitions.rpy
│  │  │  │  ├── indepth_translations.rpy
│  │  │  │  ├── options.rpy
│  │  │  │  ├── screens.rpy
│  │  │  │  ├── script.rpy
│  │  │  │  ├── tutorial_atl.rpy
│  │  │  │  ├── tutorial_director.rpy
│  │  │  │  ├── tutorial_distribute.rpy
│  │  │  │  ├── tutorial_nvlmode.rpy
│  │  │  │  ├── tutorial_playing.rpy
│  │  │  │  ├── tutorial_quickstart.rpy
│  │  │  │  ├── tutorial_screens.rpy
│  │  │  │  ├── tutorial_screen_displayables.rpy
│  │  │  │  └── tutorial_video.rpy
│  │  │  └── ukrainian
│  │  │     ├── 01example.rpy
│  │  │     ├── common.rpy
│  │  │     ├── indepth_character.rpy
│  │  │     ├── indepth_displayables.rpy
│  │  │     ├── indepth_minigame.rpy
│  │  │     ├── indepth_style.rpy
│  │  │     ├── indepth_text.rpy
│  │  │     ├── indepth_transitions.rpy
│  │  │     ├── indepth_translations.rpy
│  │  │     ├── options.rpy
│  │  │     ├── screens.rpy
│  │  │     ├── script.rpy
│  │  │     ├── tutorial_atl.rpy
│  │  │     ├── tutorial_director.rpy
│  │  │     ├── tutorial_distribute.rpy
│  │  │     ├── tutorial_nvlmode.rpy
│  │  │     ├── tutorial_playing.rpy
│  │  │     ├── tutorial_quickstart.rpy
│  │  │     ├── tutorial_screens.rpy
│  │  │     ├── tutorial_screen_displayables.rpy
│  │  │     └── tutorial_video.rpy
│  │  ├── 01director_support.rpy
│  │  ├── 01example.rpy
│  │  ├── examples.rpy
│  │  ├── exclamation.png
│  │  ├── gui.rpy
│  │  ├── indepth_character.rpy
│  │  ├── indepth_displayables.rpy
│  │  ├── indepth_minigame.rpy
│  │  ├── indepth_style.rpy
│  │  ├── indepth_text.rpy
│  │  ├── indepth_transitions.rpy
│  │  ├── indepth_translations.rpy
│  │  ├── keywords.py
│  │  ├── oa4_launch.webm
│  │  ├── options.rpy
│  │  ├── pong_beep.opus
│  │  ├── pong_boop.opus
│  │  ├── punch.opus
│  │  ├── renpyallstars.ogg
│  │  ├── screens.rpy
│  │  ├── script.rpy
│  │  ├── sunflower-slow-drag.ogg
│  │  ├── target1.png
│  │  ├── target2.png
│  │  ├── testcases.rpy
│  │  ├── tower_clock.ogg
│  │  ├── tutorial_atl.rpy
│  │  ├── tutorial_director.rpym
│  │  ├── tutorial_distribute.rpy
│  │  ├── tutorial_nvlmode.rpy
│  │  ├── tutorial_playing.rpy
│  │  ├── tutorial_quickstart.rpy
│  │  ├── tutorial_screens.rpy
│  │  ├── tutorial_screen_displayables.rpy
│  │  └── tutorial_video.rpy
│  ├── progressive_download.txt
│  └── project.json
├── unittests
│  ├── teststyles.py
│  └── __init__.py
├── .gitignore
├── add.py
├── after_checkout.sh
├── arch_design_doc.md
├── distribute.py
├── main.py
├── pyproject.toml
├── README.rst
├── renpy.py
├── run.sh
├── test_dlc.sh
└── TRANSLATORS.rst
```