 {
    'targets': [
      {
        'target_name': 'polycode',
        'type': 'executable',
        'dependencies': [
          'zlib.gyp:zlib',
          'libpng.gyp:libpng',
          'freetype.gyp:freetype',
          'lua.gyp:lua',
	      'physfs.gyp:physfs',
		  'libogg.gyp:ogg',
		  'libvorbis.gyp:libvorbis',
		  'openal-soft.gyp:OpenAL32',
		  'sdl2.gyp:SDL2',
		  'box2d.gyp:box2d',
		  'bullet.gyp:bullet',
        ],
      },
    ],
  }
