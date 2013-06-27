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
        ],
      },
    ],
  }
