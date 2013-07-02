 {
  "variables": {
        "assimp_dir%": "../third_party/assimp"
  },
  'targets': [
    {
      'target_name': 'assimp',
      'type': 'static_library',
      'sources': [
        '<(assimp_dir)/code/3DSConverter.cpp',
        '<(assimp_dir)/code/3DSLoader.cpp',
        '<(assimp_dir)/code/ACLoader.cpp',
        '<(assimp_dir)/code/ASELoader.cpp',
        '<(assimp_dir)/code/ASEParser.cpp',
        '<(assimp_dir)/code/Assimp.cpp',
        '<(assimp_dir)/code/AssimpCExport.cpp',
        '<(assimp_dir)/code/AssimpPCH.cpp',
        '<(assimp_dir)/code/B3DImporter.cpp',
        '<(assimp_dir)/code/BVHLoader.cpp',
        '<(assimp_dir)/code/BaseImporter.cpp',
        '<(assimp_dir)/code/BaseProcess.cpp',
        '<(assimp_dir)/code/BlenderDNA.cpp',
        '<(assimp_dir)/code/BlenderLoader.cpp',
        '<(assimp_dir)/code/BlenderModifier.cpp',
        '<(assimp_dir)/code/BlenderScene.cpp',
        '<(assimp_dir)/code/COBLoader.cpp',
        '<(assimp_dir)/code/CSMLoader.cpp',
        '<(assimp_dir)/code/CalcTangentsProcess.cpp',
        '<(assimp_dir)/code/ColladaExporter.cpp',
        '<(assimp_dir)/code/ColladaLoader.cpp',
        '<(assimp_dir)/code/ColladaParser.cpp',
        '<(assimp_dir)/code/ComputeUVMappingProcess.cpp',
        '<(assimp_dir)/code/ConvertToLHProcess.cpp',
        '<(assimp_dir)/code/DXFLoader.cpp',
        '<(assimp_dir)/code/DeboneProcess.cpp',
        '<(assimp_dir)/code/DefaultIOStream.cpp',
        '<(assimp_dir)/code/DefaultIOSystem.cpp',
        '<(assimp_dir)/code/DefaultLogger.cpp',
        '<(assimp_dir)/code/Exporter.cpp',
        '<(assimp_dir)/code/FindDegenerates.cpp',
        '<(assimp_dir)/code/FindInstancesProcess.cpp',
        '<(assimp_dir)/code/FindInvalidDataProcess.cpp',
        '<(assimp_dir)/code/FixNormalsStep.cpp',
        '<(assimp_dir)/code/GenFaceNormalsProcess.cpp',
        '<(assimp_dir)/code/GenVertexNormalsProcess.cpp',
        '<(assimp_dir)/code/HMPLoader.cpp',
        '<(assimp_dir)/code/IFCCurve.cpp',
        '<(assimp_dir)/code/IFCGeometry.cpp',
        '<(assimp_dir)/code/IFCLoader.cpp',
        '<(assimp_dir)/code/IFCMaterial.cpp',
        '<(assimp_dir)/code/IFCProfile.cpp',
        '<(assimp_dir)/code/IFCReaderGen.cpp',
        '<(assimp_dir)/code/IFCUtil.cpp',
        '<(assimp_dir)/code/IRRLoader.cpp',
        '<(assimp_dir)/code/IRRMeshLoader.cpp',
        '<(assimp_dir)/code/IRRShared.cpp',
        '<(assimp_dir)/code/Importer.cpp',
        '<(assimp_dir)/code/ImporterRegistry.cpp',
        '<(assimp_dir)/code/ImproveCacheLocality.cpp',
        '<(assimp_dir)/code/JoinVerticesProcess.cpp',
        '<(assimp_dir)/code/LWOAnimation.cpp',
        '<(assimp_dir)/code/LWOBLoader.cpp',
        '<(assimp_dir)/code/LWOLoader.cpp',
        '<(assimp_dir)/code/LWOMaterial.cpp',
        '<(assimp_dir)/code/LWSLoader.cpp',
        '<(assimp_dir)/code/LimitBoneWeightsProcess.cpp',
        '<(assimp_dir)/code/M3Importer.cpp',
        '<(assimp_dir)/code/MD2Loader.cpp',
        '<(assimp_dir)/code/MD3Loader.cpp',
        '<(assimp_dir)/code/MD5Loader.cpp',
        '<(assimp_dir)/code/MD5Parser.cpp',
        '<(assimp_dir)/code/MDCLoader.cpp',
        '<(assimp_dir)/code/MDLLoader.cpp',
        '<(assimp_dir)/code/MDLMaterialLoader.cpp',
        '<(assimp_dir)/code/MS3DLoader.cpp',
        '<(assimp_dir)/code/MakeVerboseFormat.cpp',
        '<(assimp_dir)/code/MaterialSystem.cpp',
        '<(assimp_dir)/code/NDOLoader.cpp',
        '<(assimp_dir)/code/NFFLoader.cpp',
        '<(assimp_dir)/code/OFFLoader.cpp',
        '<(assimp_dir)/code/ObjExporter.cpp',
        '<(assimp_dir)/code/ObjFileImporter.cpp',
        '<(assimp_dir)/code/ObjFileMtlImporter.cpp',
        '<(assimp_dir)/code/ObjFileParser.cpp',
        '<(assimp_dir)/code/OgreImporter.cpp',
        '<(assimp_dir)/code/OgreMaterial.cpp',
        '<(assimp_dir)/code/OgreMesh.cpp',
        '<(assimp_dir)/code/OgreSkeleton.cpp',
        '<(assimp_dir)/code/OptimizeGraph.cpp',
        '<(assimp_dir)/code/OptimizeMeshes.cpp',
        '<(assimp_dir)/code/PlyExporter.cpp',
        '<(assimp_dir)/code/PlyLoader.cpp',
        '<(assimp_dir)/code/PlyParser.cpp',
        '<(assimp_dir)/code/PostStepRegistry.cpp',
        '<(assimp_dir)/code/PretransformVertices.cpp',
        '<(assimp_dir)/code/ProcessHelper.cpp',
        '<(assimp_dir)/code/Q3BSPFileImporter.cpp',
        '<(assimp_dir)/code/Q3BSPFileParser.cpp',
        '<(assimp_dir)/code/Q3BSPZipArchive.cpp',
        '<(assimp_dir)/code/Q3DLoader.cpp',
        '<(assimp_dir)/code/RawLoader.cpp',
        '<(assimp_dir)/code/RemoveComments.cpp',
        '<(assimp_dir)/code/RemoveRedundantMaterials.cpp',
        '<(assimp_dir)/code/RemoveVCProcess.cpp',
        '<(assimp_dir)/code/SGSpatialSort.cpp',
        '<(assimp_dir)/code/SMDLoader.cpp',
        '<(assimp_dir)/code/STEPFileReader.cpp',
        '<(assimp_dir)/code/STLExporter.cpp',
        '<(assimp_dir)/code/STLLoader.cpp',
        '<(assimp_dir)/code/SceneCombiner.cpp',
        '<(assimp_dir)/code/ScenePreprocessor.cpp',
        '<(assimp_dir)/code/SkeletonMeshBuilder.cpp',
        '<(assimp_dir)/code/SortByPTypeProcess.cpp',
        '<(assimp_dir)/code/SpatialSort.cpp',
        '<(assimp_dir)/code/SplitByBoneCountProcess.cpp',
        '<(assimp_dir)/code/SplitLargeMeshes.cpp',
        '<(assimp_dir)/code/StandardShapes.cpp',
        '<(assimp_dir)/code/Subdivision.cpp',
        '<(assimp_dir)/code/TargetAnimation.cpp',
        '<(assimp_dir)/code/TerragenLoader.cpp',
        '<(assimp_dir)/code/TextureTransform.cpp',
        '<(assimp_dir)/code/TriangulateProcess.cpp',
        '<(assimp_dir)/code/UnrealLoader.cpp',
        '<(assimp_dir)/code/ValidateDataStructure.cpp',
        '<(assimp_dir)/code/VertexTriangleAdjacency.cpp',
        '<(assimp_dir)/code/XFileImporter.cpp',
        '<(assimp_dir)/code/XFileParser.cpp',
        # Contrib
        '<(assimp_dir)/contrib/ConvertUTF/ConvertUTF.c',
	    '<(assimp_dir)/contrib/irrXML/irrXML.cpp',
      ],
        'include_dirs': [
          '<(assimp_dir)/include',
          '<(assimp_dir)/contrib/irrXML/',
          '<(assimp_dir)/code/BoostWorkaround',
          '<(assimp_dir)/code/',
        ],
        'all_dependent_settings': {
          'include_dirs': [
            '<(assimp_dir)/include/',
            '<(assimp_dir)/contrib/irrXML/',
            '<(assimp_dir)/code/BoostWorkaround/',
            '<(assimp_dir)/code/',
          ],
      },
      'dependencies': [
	    'zlib.gyp:zlib',
	    'zlib.gyp:unzip',
	  ],
      'defines': [
		 'ASSIMP_BUILD_BOOST_WORKAROUND',
 		 ],
      'conditions': [
         ['OS=="linux"', {
           'defines': [
           ],}
         ],
      ]
    },
  ],
}
