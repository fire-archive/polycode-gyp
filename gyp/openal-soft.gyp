{
	"variables": {
		"library%": "shared_library",
		"openal_dir%": "../third_party/openal-soft"
	},

	"target_defaults": {
		"include_dirs": [
			"openal/include",
			"<(openal_dir)/include",
			"<(openal_dir)/OpenAL32/Include"
		],

		"cflags": [ "-Winline", "-Wall", "-Wextra" ],
		"defines": 
		[ "AL_BUILD_LIBRARY", "AL_ALEXT_PROTOTYPES", 
		],

		"target_conditions": [
			["_type == 'shared_library'", {
				"cflags": [ "-fPIC" ]
			}],
			["_type == 'static_library'", {
				"defines": [ "AL_LIBTYPE_STATIC" ],
				"all_dependent_settings": {
					"defines": [ "AL_LIBTYPE_STATIC" ]
				}
			}],
			["OS == 'linux'", {
				"defines": [
					"LINUX", "_GNU_SOURCE=1",	
				]
			}],
			["OS == 'win'", {
				"defines": [
					"WIN32", "_WINDOWS",
					"_WIN32", "_CRT_SECURE_NO_WARNINGS", 
					"_CRT_NONSTDC_NO_DEPRECATE", "strcasecmp=_stricmp", 
					"strncasecmp=_strnicmp", "snprintf=_snprintf", 
					"isfinite=_finite", "isnan=_isnan",
					"HAVE_WINDOWS_H", 
				]
			}]
		],

		"default_configuration": "Release",
		"configurations": {
			"Debug": {
				"cflags": [ "-g3" ],
				"msvs_settings": {
					"VCCLCompilerTool": {
						"RuntimeLibrary": 3
					}
				}
			},
			"Release": {
				"cflags": [ "-O2", "-fomit-frame-pointer" ],
				"msvs_settings": {
					"VCCLCompilerTool": {
						"RuntimeLibrary": 2
					}
				}
			}
		}
	},

	"targets": [
		{
			"type": "<(library)",
			"cflags": [ "-fvisibility=internal", "-pthread" ],
			"sources": [
				"<(openal_dir)/OpenAL32/alAuxEffectSlot.c",
				"<(openal_dir)/OpenAL32/alBuffer.c",
				"<(openal_dir)/OpenAL32/alEffect.c",
				"<(openal_dir)/OpenAL32/alError.c",
				"<(openal_dir)/OpenAL32/alExtension.c",
				"<(openal_dir)/OpenAL32/alFilter.c",
				"<(openal_dir)/OpenAL32/alListener.c",
				"<(openal_dir)/OpenAL32/alSource.c",
				"<(openal_dir)/OpenAL32/alState.c",
				"<(openal_dir)/OpenAL32/alThunk.c",
				"<(openal_dir)/Alc/ALc.c",
				"<(openal_dir)/Alc/ALu.c",
				"<(openal_dir)/Alc/alcConfig.c",
				"<(openal_dir)/Alc/alcDedicated.c",
				"<(openal_dir)/Alc/alcEcho.c",
				"<(openal_dir)/Alc/alcModulator.c",
				"<(openal_dir)/Alc/alcReverb.c",
				"<(openal_dir)/Alc/alcRing.c",
				"<(openal_dir)/Alc/alcThread.c",
				"<(openal_dir)/Alc/bs2b.c",
				"<(openal_dir)/Alc/helpers.c",
				"<(openal_dir)/Alc/hrtf.c",
				"<(openal_dir)/Alc/mixer.c",
				"<(openal_dir)/Alc/mixer_c.c",
				"<(openal_dir)/Alc/panning.c",
				"<(openal_dir)/Alc/backends/loopback.c",
				"<(openal_dir)/Alc/backends/null.c"
			],
			"conditions": [
				["OS != 'win'", {
					"target_name": "openal"
				}],
				["OS == 'win'", {
					"target_name": "OpenAL32",
					"sources": [
						"<(openal_dir)/Alc/backends/mmdevapi.c",
						"<(openal_dir)/Alc/backends/dsound.c",
						"<(openal_dir)/Alc/backends/winmm.c"
					],
					"libraries": [ "-lwinmm.lib", "-ldsound.lib", 
					"-lshell32.lib", "-lole32.lib", 
					"-lUser32.lib", 
					],
					"all_dependent_settings": {
						"include_dirs": [ "<(openal_dir)/include/AL" ]
					}
				}],
				["OS == 'linux'", {
					"sources": [
						"<(openal_dir)/Alc/backends/alsa.c",
						"<(openal_dir)/Alc/backends/pulseaudio.c"
					],
					"libraries": [ "-lrt", "-lpthread", "-ldl", "-lm" ],
					"all_dependent_settings": {
						"include_dirs": [ "<(openal_dir)/include" ]
					}
				}],
				["OS == 'mac'", {
					"sources": [
						"<(openal_dir)/Alc/backends/coreaudio.c"
					],
					"libraries": [
						"-framework AudioToolbox",
						"-framework ApplicationServices",
						"-framework AudioUnit",
						"-framework CoreAudio",
						"-lpthread", "-ldl", "-lm"
					],
					"all_dependent_settings": {
						"include_dirs": [ "include-mac" ]
					}
				}]
			]
		}
	]
}
