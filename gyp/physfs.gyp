 {
  'targets': [
    {
      'target_name': 'physfs',
      'type': 'static_library',
      'sources': [
        '../third_party/physfs/physfs.c',
        '../third_party/physfs/physfs_byteorder.c',
        '../third_party/physfs/physfs_unicode.c',
        '../third_party/physfs/platform/os2.c',
        '../third_party/physfs/platform/pocketpc.c',
        '../third_party/physfs/platform/posix.c',
        '../third_party/physfs/platform/unix.c',
        '../third_party/physfs/platform/macosx.c',
        '../third_party/physfs/platform/windows.c',
        '../third_party/physfs/archivers/dir.c',
        '../third_party/physfs/archivers/grp.c',
        '../third_party/physfs/archivers/hog.c',
        '../third_party/physfs/archivers/lzma.c',
        '../third_party/physfs/archivers/mvl.c',
        '../third_party/physfs/archivers/qpak.c',
        '../third_party/physfs/archivers/wad.c',
        '../third_party/physfs/archivers/zip.c',
        # LZMA
        '../third_party/physfs/lzma/C/7zCrc.c',
        '../third_party/physfs/lzma/C/Archive/7z/7zBuffer.c',
        '../third_party/physfs/lzma/C/Archive/7z/7zDecode.c',
        '../third_party/physfs/lzma/C/Archive/7z/7zExtract.c',
        '../third_party/physfs/lzma/C/Archive/7z/7zHeader.c',
        '../third_party/physfs/lzma/C/Archive/7z/7zIn.c',
        '../third_party/physfs/lzma/C/Archive/7z/7zItem.c',
        '../third_party/physfs/lzma/C/Archive/7z/7zMethodID.c',
        '../third_party/physfs/lzma/C/Compress/Branch/BranchX86.c',
        '../third_party/physfs/lzma/C/Compress/Branch/BranchX86_2.c',
        '../third_party/physfs/lzma/C/Compress/Lzma/LzmaDecode.c',
      ],
        'include_dirs': [
          '../third_party/physfs/',
          '../third_party/zlib/',
        ],
        'all_dependent_settings': {
          'include_dirs': [
            '../third_party/physfs/',
          ],
      },
      'defines': [
		# Thread support
		'_REENTRANT',
		'_THREAD_SAFE',	
		# Archiving formats
		'PHYSFS_SUPPORTS_ZIP',
		'PHYSFS_SUPPORTS_7Z',
		'PHYSFS_SUPPORTS_GRP',
		'PHYSFS_SUPPORTS_WAD',
		'PHYSFS_SUPPORTS_HOG',
                'PHYSFS_SUPPORTS_MVL',
		'PHYSFS_SUPPORTS_QPAK',	
		'PHYSFS_SUPPORTS_ISO9660',
 		],
      'conditions': [
        ['OS=="linux"', {
          'defines': [
	  # Todo; check headers for cdrom support	    		    
          ],}
        ],
      ]
    },
  ],
}
