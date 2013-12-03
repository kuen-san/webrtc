# Copyright (c) 2011 The WebRTC project authors. All Rights Reserved.
#
# Use of this source code is governed by a BSD-style license
# that can be found in the LICENSE file in the root of the source
# tree. An additional intellectual property rights grant can be found
# in the file PATENTS.  All contributing project authors may
# be found in the AUTHORS file in the root of the source tree.

{
  'includes': [
    '../build/common.gypi',
    'audio_coding/codecs/cng/cng.gypi',
    'audio_coding/codecs/g711/g711.gypi',
    'audio_coding/codecs/g722/g722.gypi',
    'audio_coding/codecs/ilbc/ilbc.gypi',
    'audio_coding/codecs/isac/main/source/isac.gypi',
    'audio_coding/codecs/isac/fix/source/isacfix.gypi',
    'audio_coding/codecs/pcm16b/pcm16b.gypi',
    'audio_coding/main/source/audio_coding_module.gypi',
    'audio_coding/neteq/neteq.gypi',
    'audio_coding/neteq4/neteq.gypi',
    'audio_conference_mixer/source/audio_conference_mixer.gypi',
    'audio_device/audio_device.gypi',
    'audio_processing/audio_processing.gypi',
    'bitrate_controller/bitrate_controller.gypi',
    'desktop_capture/desktop_capture.gypi',
    'media_file/source/media_file.gypi',
    'pacing/pacing.gypi',
    'remote_bitrate_estimator/remote_bitrate_estimator.gypi',
    'rtp_rtcp/source/rtp_rtcp.gypi',
    'utility/source/utility.gypi',
    'video_coding/codecs/i420/main/source/i420.gypi',
    'video_coding/main/source/video_coding.gypi',
    'video_capture/video_capture.gypi',
    'video_processing/main/source/video_processing.gypi',
    'video_render/video_render.gypi',
  ],
  'conditions': [
    ['include_opus==1', {
      'includes': ['audio_coding/codecs/opus/opus.gypi',],
    }],
    ['include_tests==1', {
      'includes': [
        'audio_coding/codecs/isac/isac_test.gypi',
        'audio_coding/codecs/isac/isacfix_test.gypi',
        'audio_processing/audio_processing_tests.gypi',
        'rtp_rtcp/test/testFec/test_fec.gypi',
        'video_coding/main/source/video_coding_test.gypi',
        'video_coding/codecs/test/video_codecs_test_framework.gypi',
        'video_coding/codecs/test_framework/test_framework.gypi',
        'video_coding/codecs/tools/video_codecs_tools.gypi',
      ], # includes
      'variables': {
        'conditions': [
          # Desktop capturer is supported only on Windows, OSX and Linux.
          ['OS=="win" or OS=="mac" or OS=="linux"', {
            'desktop_capture_supported%': 1,
          }, {
            'desktop_capture_supported%': 0,
          }],
        ],
      },
      'targets': [
        {
          'target_name': 'modules_unittests',
          'type': '<(gtest_target_type)',
          'defines': [
            '<@(audio_coding_defines)',
          ],
          'dependencies': [
            'audio_coding_module',
            'audio_processing',
            'audioproc_unittest_proto',
            'bitrate_controller',
            'CNG',
            'desktop_capture',
            'iSACFix',
            'media_file',
            'NetEq',
            'NetEq4',
            'NetEq4TestTools',
            'neteq_unittest_tools',
            'paced_sender',
            'PCM16B',  # Needed by NetEq tests.
            'remote_bitrate_estimator',
            'rtp_rtcp',
            'test_framework',
            'video_codecs_test_framework',
            'video_processing',
            'webrtc_utility',
            'webrtc_video_coding',
            '<@(neteq_dependencies)',
            '<(rbe_components_path)/remote_bitrate_estimator_components.gyp:rbe_components',
            '<(DEPTH)/testing/gmock.gyp:gmock',
            '<(DEPTH)/testing/gtest.gyp:gtest',
            '<(DEPTH)/third_party/gflags/gflags.gyp:gflags',
            '<(webrtc_root)/common_audio/common_audio.gyp:common_audio',
            '<(webrtc_root)/modules/video_coding/codecs/vp8/vp8.gyp:webrtc_vp8',
            '<(webrtc_root)/system_wrappers/source/system_wrappers.gyp:system_wrappers',
            '<(webrtc_root)/test/test.gyp:test_support_main',
            '<(webrtc_root)/common_video/common_video.gyp:frame_generator',
          ],
          'sources': [
            'audio_coding/main/acm2/acm_receiver_unittest.cc',
            'audio_coding/main/acm2/initial_delay_manager_unittest.cc',
            'audio_coding/main/acm2/nack_unittest.cc',
            'audio_coding/main/source/acm_neteq_unittest.cc',
            'audio_coding/codecs/cng/cng_unittest.cc',
            'audio_coding/codecs/isac/fix/source/filters_unittest.cc',
            'audio_coding/codecs/isac/fix/source/filterbanks_unittest.cc',
            'audio_coding/codecs/isac/fix/source/lpc_masking_model_unittest.cc',
            'audio_coding/codecs/isac/fix/source/transform_unittest.cc',
            'audio_coding/codecs/isac/main/source/isac_unittest.cc',
            'audio_coding/codecs/opus/opus_unittest.cc',
            'audio_coding/neteq4/audio_multi_vector_unittest.cc',
            'audio_coding/neteq4/audio_vector_unittest.cc',
            'audio_coding/neteq4/background_noise_unittest.cc',
            'audio_coding/neteq4/buffer_level_filter_unittest.cc',
            'audio_coding/neteq4/comfort_noise_unittest.cc',
            'audio_coding/neteq4/decision_logic_unittest.cc',
            'audio_coding/neteq4/decoder_database_unittest.cc',
            'audio_coding/neteq4/delay_manager_unittest.cc',
            'audio_coding/neteq4/delay_peak_detector_unittest.cc',
            'audio_coding/neteq4/dsp_helper_unittest.cc',
            'audio_coding/neteq4/dtmf_buffer_unittest.cc',
            'audio_coding/neteq4/dtmf_tone_generator_unittest.cc',
            'audio_coding/neteq4/expand_unittest.cc',
            'audio_coding/neteq4/merge_unittest.cc',
            'audio_coding/neteq4/neteq_external_decoder_unittest.cc',
            'audio_coding/neteq4/neteq_impl_unittest.cc',
            'audio_coding/neteq4/neteq_stereo_unittest.cc',
            'audio_coding/neteq4/neteq_unittest.cc',
            'audio_coding/neteq4/normal_unittest.cc',
            'audio_coding/neteq4/packet_buffer_unittest.cc',
            'audio_coding/neteq4/payload_splitter_unittest.cc',
            'audio_coding/neteq4/post_decode_vad_unittest.cc',
            'audio_coding/neteq4/random_vector_unittest.cc',
            'audio_coding/neteq4/sync_buffer_unittest.cc',
            'audio_coding/neteq4/timestamp_scaler_unittest.cc',
            'audio_coding/neteq4/time_stretch_unittest.cc',
            'audio_coding/neteq4/mock/mock_audio_decoder.h',
            'audio_coding/neteq4/mock/mock_audio_vector.h',
            'audio_coding/neteq4/mock/mock_buffer_level_filter.h',
            'audio_coding/neteq4/mock/mock_decoder_database.h',
            'audio_coding/neteq4/mock/mock_delay_manager.h',
            'audio_coding/neteq4/mock/mock_delay_peak_detector.h',
            'audio_coding/neteq4/mock/mock_dtmf_buffer.h',
            'audio_coding/neteq4/mock/mock_dtmf_tone_generator.h',
            'audio_coding/neteq4/mock/mock_external_decoder_pcm16b.h',
            'audio_coding/neteq4/mock/mock_packet_buffer.h',
            'audio_coding/neteq4/mock/mock_payload_splitter.h',
            'audio_processing/aec/system_delay_unittest.cc',
            'audio_processing/aec/echo_cancellation_unittest.cc',
            'audio_processing/echo_cancellation_impl_unittest.cc',
            'audio_processing/test/audio_processing_unittest.cc',
            'audio_processing/utility/delay_estimator_unittest.cc',
            'audio_processing/utility/ring_buffer_unittest.cc',
            'bitrate_controller/bitrate_controller_unittest.cc',
            'desktop_capture/desktop_and_cursor_composer_unittest.cc',
            'desktop_capture/desktop_region_unittest.cc',
            'desktop_capture/differ_block_unittest.cc',
            'desktop_capture/differ_unittest.cc',
            'desktop_capture/mouse_cursor_monitor_unittest.cc',
            'desktop_capture/screen_capturer_helper_unittest.cc',
            'desktop_capture/screen_capturer_mac_unittest.cc',
            'desktop_capture/screen_capturer_mock_objects.h',
            'desktop_capture/screen_capturer_unittest.cc',
            'desktop_capture/window_capturer_unittest.cc',
            "desktop_capture/win/cursor_unittest.cc",
            "desktop_capture/win/cursor_unittest_resources.h",
            "desktop_capture/win/cursor_unittest_resources.rc",
            'media_file/source/media_file_unittest.cc',
            'module_common_types_unittest.cc',
            'pacing/paced_sender_unittest.cc',
            'remote_bitrate_estimator/include/mock/mock_remote_bitrate_observer.h',
            'remote_bitrate_estimator/rate_statistics_unittest.cc',
            'remote_bitrate_estimator/remote_bitrate_estimator_single_stream_unittest.cc',
            'remote_bitrate_estimator/remote_bitrate_estimator_unittest_helper.cc',
            'remote_bitrate_estimator/remote_bitrate_estimator_unittest_helper.h',
            'remote_bitrate_estimator/remote_bitrate_estimators_test.cc',
            'remote_bitrate_estimator/rtp_to_ntp_unittest.cc',
            'remote_bitrate_estimator/test/bwe_test_framework.cc',
            'remote_bitrate_estimator/test/bwe_test_framework.h',
            'remote_bitrate_estimator/test/bwe_test_framework_unittest.cc',
            'remote_bitrate_estimator/test/bwe_test_logging.cc',
            'remote_bitrate_estimator/test/bwe_test_logging.h',
            'remote_bitrate_estimator/test/bwe_test.cc',
            'remote_bitrate_estimator/test/bwe_test.h',
            'rtp_rtcp/source/mock/mock_rtp_payload_strategy.h',
            'rtp_rtcp/source/byte_io_unittest.cc',
            'rtp_rtcp/source/fec_receiver_unittest.cc',
            'rtp_rtcp/source/fec_test_helper.cc',
            'rtp_rtcp/source/fec_test_helper.h',
            'rtp_rtcp/source/nack_rtx_unittest.cc',
            'rtp_rtcp/source/producer_fec_unittest.cc',
            'rtp_rtcp/source/receive_statistics_unittest.cc',
            'rtp_rtcp/source/rtcp_format_remb_unittest.cc',
            'rtp_rtcp/source/rtcp_sender_unittest.cc',
            'rtp_rtcp/source/rtcp_receiver_unittest.cc',
            'rtp_rtcp/source/rtp_fec_unittest.cc',
            'rtp_rtcp/source/rtp_format_vp8_unittest.cc',
            'rtp_rtcp/source/rtp_format_vp8_test_helper.cc',
            'rtp_rtcp/source/rtp_format_vp8_test_helper.h',
            'rtp_rtcp/source/rtp_packet_history_unittest.cc',
            'rtp_rtcp/source/rtp_payload_registry_unittest.cc',
            'rtp_rtcp/source/rtp_rtcp_impl_unittest.cc',
            'rtp_rtcp/source/rtp_utility_unittest.cc',
            'rtp_rtcp/source/rtp_header_extension_unittest.cc',
            'rtp_rtcp/source/rtp_sender_unittest.cc',
            'rtp_rtcp/source/vp8_partition_aggregator_unittest.cc',
            'rtp_rtcp/test/testAPI/test_api.cc',
            'rtp_rtcp/test/testAPI/test_api.h',
            'rtp_rtcp/test/testAPI/test_api_audio.cc',
            'rtp_rtcp/test/testAPI/test_api_rtcp.cc',
            'rtp_rtcp/test/testAPI/test_api_video.cc',
            'utility/source/audio_frame_operations_unittest.cc',
            'video_coding/codecs/test/packet_manipulator_unittest.cc',
            'video_coding/codecs/test/stats_unittest.cc',
            'video_coding/codecs/test/videoprocessor_unittest.cc',
            'video_coding/codecs/vp8/default_temporal_layers_unittest.cc',
            'video_coding/codecs/vp8/reference_picture_selection_unittest.cc',
            'video_coding/main/interface/mock/mock_vcm_callbacks.h',
            'video_coding/main/source/decoding_state_unittest.cc',
            'video_coding/main/source/jitter_buffer_unittest.cc',
            'video_coding/main/source/media_optimization_unittest.cc',
            'video_coding/main/source/receiver_unittest.cc',
            'video_coding/main/source/session_info_unittest.cc',
            'video_coding/main/source/timing_unittest.cc',
            'video_coding/main/source/video_coding_robustness_unittest.cc',
            'video_coding/main/source/video_receiver_unittest.cc',
            'video_coding/main/source/video_sender_unittest.cc',
            'video_coding/main/source/qm_select_unittest.cc',
            'video_coding/main/source/test/stream_generator.cc',
            'video_coding/main/source/test/stream_generator.h',
            'video_coding/main/test/pcap_file_reader.cc',
            'video_coding/main/test/pcap_file_reader_unittest.cc',
            'video_coding/main/test/rtp_file_reader.cc',
            'video_coding/main/test/rtp_file_reader_unittest.cc',
            'video_processing/main/test/unit_test/brightness_detection_test.cc',
            'video_processing/main/test/unit_test/color_enhancement_test.cc',
            'video_processing/main/test/unit_test/content_metrics_test.cc',
            'video_processing/main/test/unit_test/deflickering_test.cc',
            'video_processing/main/test/unit_test/denoising_test.cc',
            'video_processing/main/test/unit_test/video_processing_unittest.cc',
            'video_processing/main/test/unit_test/video_processing_unittest.h',
          ],
          'conditions': [
            ['enable_bwe_test_logging==1', {
              'defines': [ 'BWE_TEST_LOGGING_COMPILE_TIME_ENABLE=1' ],
            }, {
              'defines': [ 'BWE_TEST_LOGGING_COMPILE_TIME_ENABLE=0' ],
              'sources!': [
                'remote_bitrate_estimator/test/bwe_test_logging.cc'
              ],
            }],
            # Run screen/window capturer tests only on platforms where they are
            # supported.
            ['desktop_capture_supported==0', {
              'sources!': [
                'desktop_capture/desktop_and_cursor_composer_unittest.cc',
                'desktop_capture/mouse_cursor_monitor_unittest.cc',
                'desktop_capture/screen_capturer_helper_unittest.cc',
                'desktop_capture/screen_capturer_mac_unittest.cc',
                'desktop_capture/screen_capturer_mock_objects.h',
                'desktop_capture/screen_capturer_unittest.cc',
                'desktop_capture/window_capturer_unittest.cc',
              ],
            }],
            ['prefer_fixed_point==1', {
              'defines': [ 'WEBRTC_AUDIOPROC_FIXED_PROFILE' ],
            }, {
              'defines': [ 'WEBRTC_AUDIOPROC_FLOAT_PROFILE' ],
            }],
            ['enable_protobuf==1', {
              'defines': [ 'WEBRTC_AUDIOPROC_DEBUG_DUMP' ],
            }],
            ['build_libvpx==1', {
              'dependencies': [
                '<(DEPTH)/third_party/libvpx/libvpx.gyp:libvpx',
              ],
            }],
            # TODO(henrike): remove build_with_chromium==1 when the bots are
            # using Chromium's buildbots.
            ['build_with_chromium==1 and OS=="android" and gtest_target_type=="shared_library"', {
              'dependencies': [
                '<(DEPTH)/testing/android/native_test.gyp:native_test_native_code',
              ],
            }],
          ],
          # Disable warnings to enable Win64 build, issue 1323.
          'msvs_disabled_warnings': [
            4267,  # size_t to int truncation.
          ],
        },
        {
          'target_name': 'modules_tests',
          'type': '<(gtest_target_type)',
          'dependencies': [
            'audio_coding_module',
            'rtp_rtcp',
            'test_framework',
            'video_codecs_test_framework',
            'webrtc_utility',
            'webrtc_video_coding',
            '<(DEPTH)/testing/gtest.gyp:gtest',
            '<(webrtc_root)/common_video/common_video.gyp:common_video',
            '<(webrtc_root)/modules/video_coding/codecs/vp8/vp8.gyp:webrtc_vp8',
            '<(webrtc_root)/system_wrappers/source/system_wrappers.gyp:system_wrappers',
            '<(webrtc_root)/test/metrics.gyp:metrics',
            '<(webrtc_root)/test/test.gyp:test_support',
            '<(webrtc_root)/test/test.gyp:test_support_main',
          ],
          'defines': [
            '<@(audio_coding_defines)',
          ],
          'sources': [
            'audio_coding/main/test/ACMTest.cc',
            'audio_coding/main/test/APITest.cc',
            'audio_coding/main/test/Channel.cc',
            'audio_coding/main/test/dual_stream_unittest.cc',
            'audio_coding/main/test/EncodeDecodeTest.cc',
            'audio_coding/main/test/iSACTest.cc',
            'audio_coding/main/test/opus_test.cc',
            'audio_coding/main/test/PCMFile.cc',
            'audio_coding/main/test/RTPFile.cc',
            'audio_coding/main/test/SpatialAudio.cc',
            'audio_coding/main/test/TestAllCodecs.cc',
            'audio_coding/main/test/target_delay_unittest.cc',
            'audio_coding/main/test/Tester.cc',
            'audio_coding/main/test/TestFEC.cc',
            'audio_coding/main/test/TestStereo.cc',
            'audio_coding/main/test/TestVADDTX.cc',
            'audio_coding/main/test/TimedTrace.cc',
            'audio_coding/main/test/TwoWayCommunication.cc',
            'audio_coding/main/test/initial_delay_unittest.cc',
            'audio_coding/main/test/utility.cc',
            'rtp_rtcp/test/testFec/test_fec.cc',
            'video_coding/codecs/test/videoprocessor_integrationtest.cc',
            'video_coding/codecs/vp8/test/vp8_impl_unittest.cc',
          ],
          'conditions': [
            # TODO(henrike): remove build_with_chromium==1 when the bots are
            # using Chromium's buildbots.
            ['build_with_chromium==1 and OS=="android" and gtest_target_type=="shared_library"', {
              'dependencies': [
                '<(DEPTH)/testing/android/native_test.gyp:native_test_native_code',
              ],
            }],
          ],
        },
      ],
      'conditions': [
        # TODO(henrike): remove build_with_chromium==1 when the bots are using
        # Chromium's buildbots.
        ['build_with_chromium==1 and OS=="android" and gtest_target_type=="shared_library"', {
          'targets': [
            {
              'target_name': 'modules_unittests_apk_target',
              'type': 'none',
              'dependencies': [
                '<(apk_tests_path):modules_unittests_apk',
              ],
            },
            {
              'target_name': 'modules_tests_apk_target',
              'type': 'none',
              'dependencies': [
                '<(apk_tests_path):modules_tests_apk',
              ],
            },
          ],
        }],
        ['test_isolation_mode != "noop"', {
          'targets': [
            {
              'target_name': 'modules_tests_run',
              'type': 'none',
              'dependencies': [
                'modules_tests',
              ],
              'includes': [
                '../build/isolate.gypi',
                'modules_tests.isolate',
              ],
              'sources': [
                'modules_tests.isolate',
              ],
            },
            {
              'target_name': 'modules_unittests_run',
              'type': 'none',
              'dependencies': [
                'modules_unittests',
              ],
              'includes': [
                '../build/isolate.gypi',
                'modules_unittests.isolate',
              ],
              'sources': [
                'modules_unittests.isolate',
              ],
            },
          ],
        }],
      ],
    }], # include_tests
  ], # conditions
}
