import requests
import json
import pprint

seed_list = [
  {
    "id": "23e92c1c-1c4f-469c-8cf0-74200a6b05c8",
    "url": "https://ll.thespacedevs.com/2.2.0/launch/23e92c1c-1c4f-469c-8cf0-74200a6b05c8/",
    "slug": "hapith-i-test-flight",
    "name": "Hapith I | Test Flight",
    "status": {
      "id": 8,
      "name": "To Be Confirmed",
      "abbrev": "TBC",
      "description": "Awaiting official confirmation - current date is known with some certainty."
    },
    "last_updated": "2021-09-11T03:13:45Z",
    "net": "2021-09-12T20:30:00Z",
    "window_end": "2021-09-13T08:30:00Z",
    "window_start": "2021-09-12T20:30:00Z",
    "probability": "",
    "holdreason": "",
    "failreason": "",
    "hashtag": "",
    "launch_service_provider": {
      "id": 1029,
      "url": "https://ll.thespacedevs.com/2.2.0/agencies/1029/",
      "name": "TiSPACE",
      "type": "Private"
    },
    "rocket": {
      "id": 7450,
      "configuration": {
        "id": 474,
        "url": "https://ll.thespacedevs.com/2.2.0/config/launcher/474/",
        "name": "Hapith I",
        "family": "Hapith",
        "full_name": "Hapith I",
        "variant": "I"
      }
    },
    "mission": {
      "id": 5842,
      "name": "Test Flight",
      "description": "The first Hapith I launch will be testing TiSPACE's hybrid rocket engine technology in preparation for the future Hapith V launch vehicle. Targeting 250 km altitude, the test launch campaign will also support of the development of the Whalers Way Orbital Launch Complex in South Australia, operated by Southern Launch.",
      "launch_designator": "",
      "type": "Test Flight",
      "orbit": {
        "id": 15,
        "name": "Suborbital",
        "abbrev": "Sub"
      }
    },
    "pad": {
      "id": 197,
      "url": "https://ll.thespacedevs.com/2.2.0/pad/197/",
      "agency_id": 1028,
      "name": "Pad 1",
      "info_url": "https://www.southernlaunch.space/whalers-way-orbital-launch-complex",
      "wiki_url": "https://en.wikipedia.org/wiki/Whalers_Way_Orbital_Launch_Complex",
      "map_url": "https://www.google.com/maps?q=-34.937822,135.630035",
      "latitude": "-34.937822",
      "longitude": "135.630035",
      "location": {
        "id": 156,
        "url": "https://ll.thespacedevs.com/2.2.0/location/156/",
        "name": "Whalers Way Orbital Launch Complex",
        "country_code": "AUS",
        "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/location_whalers_way_orbital_launch_complex_20210910042508.jpg",
        "total_launch_count": 0,
        "total_landing_count": 0
      },
      "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/pad_whalers_way_orbital_launch_complex_20210910042853.jpg",
      "total_launch_count": 0
    },
    "webcast_live": "",
    "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/hapith_i_image_20210911031658.jpg",
    "infographic": "",
    "program": []
  },
  {
    "id": "360fe91d-17ae-45b1-a636-340a27c1e6f8",
    "url": "https://ll.thespacedevs.com/2.2.0/launch/360fe91d-17ae-45b1-a636-340a27c1e6f8/",
    "slug": "long-march-2cyz-1s-yaogan-32-02",
    "name": "Long March 2C/YZ-1S | Yaogan-32-02",
    "status": {
      "id": 1,
      "name": "Go for Launch",
      "abbrev": "Go",
      "description": "Current T-0 confirmed by official or reliable sources."
    },
    "last_updated": "2021-09-10T05:29:35Z",
    "net": "2021-09-13T07:45:00Z",
    "window_end": "2021-09-13T08:04:00Z",
    "window_start": "2021-09-13T07:36:00Z",
    "probability": "",
    "holdreason": "",
    "failreason": "",
    "hashtag": "",
    "launch_service_provider": {
      "id": 88,
      "url": "https://ll.thespacedevs.com/2.2.0/agencies/88/",
      "name": "China Aerospace Science and Technology Corporation",
      "type": "Government"
    },
    "rocket": {
      "id": 7446,
      "configuration": {
        "id": 156,
        "url": "https://ll.thespacedevs.com/2.2.0/config/launcher/156/",
        "name": "Long March 2C/YZ-1S",
        "family": "Long March 2",
        "full_name": "Long March 2C/YZ-1S",
        "variant": "C/YZ-1S"
      }
    },
    "mission": {
      "id": 5839,
      "name": "Yaogan-32-02",
      "description": "Yaogan is a series of Chinese reconnaissance satellites.",
      "launch_designator": "",
      "type": "Government/Top Secret",
      "orbit": {
        "id": 17,
        "name": "Sun-Synchronous Orbit",
        "abbrev": "SSO"
      }
    },
    "pad": {
      "id": 22,
      "url": "https://ll.thespacedevs.com/2.2.0/pad/22/",
      "agency_id": "",
      "name": "Launch Area 4 (SLS-2 / 603)",
      "info_url": "",
      "wiki_url": "https://en.wikipedia.org/wiki/Jiuquan_Launch_Area_4",
      "map_url": "http://maps.google.com/maps?q=40.960556,100.298333",
      "latitude": "40.960556",
      "longitude": "100.298333",
      "location": {
        "id": 17,
        "url": "https://ll.thespacedevs.com/2.2.0/location/17/",
        "name": "Jiuquan, People's Republic of China",
        "country_code": "CHN",
        "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/location_17_20200803142429.jpg",
        "total_launch_count": 146,
        "total_landing_count": 0
      },
      "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/pad_22_20200803143437.jpg",
      "total_launch_count": 72
    },
    "webcast_live": "",
    "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/long_march_2c__image_20210908193511.jpeg",
    "infographic": "",
    "program": []
  },
  {
    "id": "6b9f9fe6-7f94-498b-a664-7c9e42dbe76d",
    "url": "https://ll.thespacedevs.com/2.2.0/launch/6b9f9fe6-7f94-498b-a664-7c9e42dbe76d/",
    "slug": "falcon-9-block-5-starlink-group-2-1",
    "name": "Falcon 9 Block 5 | Starlink Group 2-1",
    "status": {
      "id": 1,
      "name": "Go for Launch",
      "abbrev": "Go",
      "description": "Current T-0 confirmed by official or reliable sources."
    },
    "last_updated": "2021-09-12T12:59:11Z",
    "net": "2021-09-14T03:55:00Z",
    "window_end": "2021-09-14T03:55:00Z",
    "window_start": "2021-09-14T03:55:00Z",
    "probability": "",
    "holdreason": "",
    "failreason": "",
    "hashtag": "",
    "launch_service_provider": {
      "id": 121,
      "url": "https://ll.thespacedevs.com/2.2.0/agencies/121/",
      "name": "SpaceX",
      "type": "Commercial"
    },
    "rocket": {
      "id": 2958,
      "configuration": {
        "id": 164,
        "url": "https://ll.thespacedevs.com/2.2.0/config/launcher/164/",
        "name": "Falcon 9",
        "family": "Falcon",
        "full_name": "Falcon 9 Block 5",
        "variant": "Block 5"
      }
    },
    "mission": {
      "id": 1380,
      "name": "Starlink Group 2-1",
      "description": "A batch of 60 satellites for Starlink mega-constellation - SpaceX's project for space-based Internet communication system.",
      "launch_designator": "",
      "type": "Communications",
      "orbit": {
        "id": 13,
        "name": "Polar Orbit",
        "abbrev": "PO"
      }
    },
    "pad": {
      "id": 16,
      "url": "https://ll.thespacedevs.com/2.2.0/pad/16/",
      "agency_id": "",
      "name": "Space Launch Complex 4E",
      "info_url": "",
      "wiki_url": "",
      "map_url": "http://maps.google.com/maps?q=34.632+N,+120.611+W",
      "latitude": "34.632",
      "longitude": "-120.611",
      "location": {
        "id": 11,
        "url": "https://ll.thespacedevs.com/2.2.0/location/11/",
        "name": "Vandenberg SFB, CA, USA",
        "country_code": "USA",
        "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/location_11_20200803142416.jpg",
        "total_launch_count": 689,
        "total_landing_count": 3
      },
      "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/pad_16_20200803143532.jpg",
      "total_launch_count": 84
    },
    "webcast_live": "",
    "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/falcon2520925_image_20210619160237.png",
    "infographic": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/falcon2520925_infographic_20210911033329.jpg",
    "program": []
  },
  {
    "id": "0834f42e-8b04-4026-a3e1-df7a0d570bba",
    "url": "https://ll.thespacedevs.com/2.2.0/launch/0834f42e-8b04-4026-a3e1-df7a0d570bba/",
    "slug": "soyuz-21bfregat-m-oneweb-10",
    "name": "Soyuz 2.1b/Fregat-M | OneWeb 10",
    "status": {
      "id": 8,
      "name": "To Be Confirmed",
      "abbrev": "TBC",
      "description": "Awaiting official confirmation - current date is known with some certainty."
    },
    "last_updated": "2021-09-07T10:13:25Z",
    "net": "2021-09-14T18:07:00Z",
    "window_end": "2021-09-14T18:07:00Z",
    "window_start": "2021-09-14T18:07:00Z",
    "probability": "",
    "holdreason": "",
    "failreason": "",
    "hashtag": "",
    "launch_service_provider": {
      "id": 115,
      "url": "https://ll.thespacedevs.com/2.2.0/agencies/115/",
      "name": "Arianespace",
      "type": "Commercial"
    },
    "rocket": {
      "id": 2856,
      "configuration": {
        "id": 134,
        "url": "https://ll.thespacedevs.com/2.2.0/config/launcher/134/",
        "name": "Soyuz 2.1b/Fregat-M",
        "family": "Soyuz",
        "full_name": "Soyuz 2.1b Fregat-M",
        "variant": "Fregat-M"
      }
    },
    "mission": {
      "id": 1270,
      "name": "OneWeb 10",
      "description": "A batch of 34 satellites for the OneWeb satellite constellation, which is intended to provide global Internet broadband service for individual consumers. The constellation is planned to have around 648 microsatellites (of which 60 are spares), around 150 kg each, operating in Ku-band from low Earth orbit.",
      "launch_designator": "",
      "type": "Communications",
      "orbit": {
        "id": 13,
        "name": "Polar Orbit",
        "abbrev": "PO"
      }
    },
    "pad": {
      "id": 20,
      "url": "https://ll.thespacedevs.com/2.2.0/pad/20/",
      "agency_id": "",
      "name": "31/6",
      "info_url": "",
      "wiki_url": "",
      "map_url": "http://maps.google.com/maps?q=45.996+N,+63.564+E",
      "latitude": "45.996034",
      "longitude": "63.564003",
      "location": {
        "id": 15,
        "url": "https://ll.thespacedevs.com/2.2.0/location/15/",
        "name": "Baikonur Cosmodrome, Republic of Kazakhstan",
        "country_code": "KAZ",
        "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/location_15_20200803142517.jpg",
        "total_launch_count": 1522,
        "total_landing_count": 0
      },
      "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/pad_20_20200803143516.jpg",
      "total_launch_count": 393
    },
    "webcast_live": "",
    "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/soyuz25202.1b_image_20210520085936.jpeg",
    "infographic": "",
    "program": []
  },
  {
    "id": "621d64e6-0513-45dc-8ffa-c9fd56518398",
    "url": "https://ll.thespacedevs.com/2.2.0/launch/621d64e6-0513-45dc-8ffa-c9fd56518398/",
    "slug": "falcon-9-block-5-inspiration4",
    "name": "Falcon 9 Block 5 | Inspiration4",
    "status": {
      "id": 1,
      "name": "Go for Launch",
      "abbrev": "Go",
      "description": "Current T-0 confirmed by official or reliable sources."
    },
    "last_updated": "2021-09-12T17:03:27Z",
    "net": "2021-09-16T00:01:00Z",
    "window_end": "2021-09-16T00:24:00Z",
    "window_start": "2021-09-16T00:01:00Z",
    "probability": 70,
    "holdreason": "",
    "failreason": "",
    "hashtag": "Inspiration4",
    "launch_service_provider": {
      "id": 121,
      "url": "https://ll.thespacedevs.com/2.2.0/agencies/121/",
      "name": "SpaceX",
      "type": "Commercial"
    },
    "rocket": {
      "id": 2825,
      "configuration": {
        "id": 164,
        "url": "https://ll.thespacedevs.com/2.2.0/config/launcher/164/",
        "name": "Falcon 9",
        "family": "Falcon",
        "full_name": "Falcon 9 Block 5",
        "variant": "Block 5"
      }
    },
    "mission": {
      "id": 1232,
      "name": "Inspiration4",
      "description": "Inspiration4 is the world\u2019s first all-commercial astronaut mission to orbit. Jared Isaacman, founder and CEO of Shift4 Payments, is donating the three seats alongside him aboard Dragon to individuals from the general public. The Inspiration4 crew will receive commercial astronaut training by SpaceX on the Falcon 9 launch vehicle and Dragon spacecraft, orbital mechanics, operating in microgravity, zero gravity, and other forms of stress testing. They will go through emergency preparedness training, spacesuit and spacecraft ingress and egress exercises, as well as partial and full mission simulations.\r\nThe Crew Dragon spacecraft will remain in a 540 km high orbit for three days before reentering Earth's atmosphere for a soft water landing off the coast of Florida.",
      "launch_designator": "",
      "type": "Human Exploration",
      "orbit": {
        "id": 8,
        "name": "Low Earth Orbit",
        "abbrev": "LEO"
      }
    },
    "pad": {
      "id": 87,
      "url": "https://ll.thespacedevs.com/2.2.0/pad/87/",
      "agency_id": "",
      "name": "Launch Complex 39A",
      "info_url": "",
      "wiki_url": "https://en.wikipedia.org/wiki/Kennedy_Space_Center_Launch_Complex_39#Launch_Pad_39A",
      "map_url": "http://maps.google.com/maps?q=28.608+N,+80.604+W",
      "latitude": "28.60822681",
      "longitude": "-80.60428186",
      "location": {
        "id": 27,
        "url": "https://ll.thespacedevs.com/2.2.0/location/27/",
        "name": "Kennedy Space Center, FL, USA",
        "country_code": "USA",
        "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/location_27_20200803142447.jpg",
        "total_launch_count": 190,
        "total_landing_count": 0
      },
      "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/pad_87_20200803143537.jpg",
      "total_launch_count": 133
    },
    "webcast_live": "",
    "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/falcon2520925_image_20210310075452.jpeg",
    "infographic": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/falcon2520925_infographic_20210911160456.jpg",
    "program": []
  },
  {
    "id": "cf0a0e4c-ce72-4b50-af07-016326cbceff",
    "url": "https://ll.thespacedevs.com/2.2.0/launch/cf0a0e4c-ce72-4b50-af07-016326cbceff/",
    "slug": "long-march-7-tianzhou-3",
    "name": "Long March 7  | Tianzhou-3",
    "status": {
      "id": 2,
      "name": "To Be Determined",
      "abbrev": "TBD",
      "description": "Current date is a 'No Earlier Than' estimation based on unreliable or interpreted sources."
    },
    "last_updated": "2021-08-12T06:35:45Z",
    "net": "2021-09-20T00:00:00Z",
    "window_end": "2021-09-20T00:00:00Z",
    "window_start": "2021-09-20T00:00:00Z",
    "probability": "",
    "holdreason": "",
    "failreason": "",
    "hashtag": "",
    "launch_service_provider": {
      "id": 88,
      "url": "https://ll.thespacedevs.com/2.2.0/agencies/88/",
      "name": "China Aerospace Science and Technology Corporation",
      "type": "Government"
    },
    "rocket": {
      "id": 2864,
      "configuration": {
        "id": 100,
        "url": "https://ll.thespacedevs.com/2.2.0/config/launcher/100/",
        "name": "Long March 7",
        "family": "Long March 7",
        "full_name": "Long March 7",
        "variant": ""
      }
    },
    "mission": {
      "id": 1280,
      "name": "Tianzhou-3",
      "description": "Second cargo delivery mission to the Chinese large modular space station.",
      "launch_designator": "",
      "type": "Resupply",
      "orbit": {
        "id": 8,
        "name": "Low Earth Orbit",
        "abbrev": "LEO"
      }
    },
    "pad": {
      "id": 78,
      "url": "https://ll.thespacedevs.com/2.2.0/pad/78/",
      "agency_id": "",
      "name": "Wenchang",
      "info_url": "",
      "wiki_url": "https://en.wikipedia.org/wiki/Wenchang_Satellite_Launch_Center",
      "map_url": "http://maps.google.com/maps?q=19.614354,110.951057",
      "latitude": "19.614354",
      "longitude": "110.951057",
      "location": {
        "id": 8,
        "url": "https://ll.thespacedevs.com/2.2.0/location/8/",
        "name": "Wenchang Satellite Launch Center, People's Republic of China",
        "country_code": "CHN",
        "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/location_8_20200803142445.jpg",
        "total_launch_count": 13,
        "total_landing_count": 0
      },
      "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/pad_78_20200803143548.jpg",
      "total_launch_count": 11
    },
    "webcast_live": "",
    "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/long_march_7_image_20210513083007.jpeg",
    "infographic": "",
    "program": [
      {
        "id": 19,
        "url": "https://ll.thespacedevs.com/2.2.0/program/19/",
        "name": "Tiangong space station",
        "description": "The Tiangong space station is a space station placed in Low Earth orbit between 340 and 450 km above the surface.",
        "agencies": [
          {
            "id": 88,
            "url": "https://ll.thespacedevs.com/2.2.0/agencies/88/",
            "name": "China Aerospace Science and Technology Corporation",
            "type": "Government"
          }
        ],
        "image_url": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/program_images/chinese2520spa_program_20210608105528.png",
        "start_date": "2021-04-29T03:23:00Z",
        "end_date": "",
        "info_url": "",
        "wiki_url": "https://en.wikipedia.org/wiki/Tiangong_space_station",
        "mission_patches": []
      }
    ]
  },
  {
    "id": "f8a96988-9ba4-4480-84c4-496492e67e23",
    "url": "https://ll.thespacedevs.com/2.2.0/launch/f8a96988-9ba4-4480-84c4-496492e67e23/",
    "slug": "atlas-v-401-landsat-9",
    "name": "Atlas V 401 | Landsat 9",
    "status": {
      "id": 8,
      "name": "To Be Confirmed",
      "abbrev": "TBC",
      "description": "Awaiting official confirmation - current date is known with some certainty."
    },
    "last_updated": "2021-08-28T09:30:18Z",
    "net": "2021-09-23T18:11:00Z",
    "window_end": "2021-09-23T18:11:00Z",
    "window_start": "2021-09-23T18:11:00Z",
    "probability": -1,
    "holdreason": "",
    "failreason": "",
    "hashtag": "",
    "launch_service_provider": {
      "id": 124,
      "url": "https://ll.thespacedevs.com/2.2.0/agencies/124/",
      "name": "United Launch Alliance",
      "type": "Commercial"
    },
    "rocket": {
      "id": 166,
      "configuration": {
        "id": 16,
        "url": "https://ll.thespacedevs.com/2.2.0/config/launcher/16/",
        "name": "Atlas V 401",
        "family": "Atlas",
        "full_name": "Atlas V 401",
        "variant": "401"
      }
    },
    "mission": {
      "id": 464,
      "name": "Landsat 9",
      "description": "Landsat 9 is a partnership between NASA and the U.S. Geological Survey to continue the Landsat program\u00e2\u20ac\u2122s critical role in monitoring, understanding and managing the land resources needed to sustain human life. Landsat 9, like Landsat 8, will have a higher imaging capacity than past Landsats, allowing more valuable data to be added to the Landsat\u00e2\u20ac\u2122s global land archive. Satellite will operaite in sun-synchronous orbit at an altitude of 705 km and has a mission lifetime of 5 years.",
      "launch_designator": "",
      "type": "Earth Science",
      "orbit": {
        "id": 17,
        "name": "Sun-Synchronous Orbit",
        "abbrev": "SSO"
      }
    },
    "pad": {
      "id": 24,
      "url": "https://ll.thespacedevs.com/2.2.0/pad/24/",
      "agency_id": 161,
      "name": "Space Launch Complex 3E",
      "info_url": "",
      "wiki_url": "",
      "map_url": "http://maps.google.com/maps?q=34.640+N,+120.5895+W",
      "latitude": "34.64",
      "longitude": "-120.5895",
      "location": {
        "id": 11,
        "url": "https://ll.thespacedevs.com/2.2.0/location/11/",
        "name": "Vandenberg SFB, CA, USA",
        "country_code": "USA",
        "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/location_11_20200803142416.jpg",
        "total_launch_count": 689,
        "total_landing_count": 3
      },
      "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/pad_24_20200803143552.jpg",
      "total_launch_count": 46
    },
    "webcast_live": "",
    "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/atlas2520v2520401_image_20190224012334.jpeg",
    "infographic": "",
    "program": []
  },
  {
    "id": "30412a48-cb4d-43d6-a304-6ae5f062504f",
    "url": "https://ll.thespacedevs.com/2.2.0/launch/30412a48-cb4d-43d6-a304-6ae5f062504f/",
    "slug": "kuaizhou-1a-jilin-1-02d",
    "name": "Kuaizhou-1A | Jilin-1-02D",
    "status": {
      "id": 2,
      "name": "To Be Determined",
      "abbrev": "TBD",
      "description": "Current date is a 'No Earlier Than' estimation based on unreliable or interpreted sources."
    },
    "last_updated": "2021-08-21T07:07:57Z",
    "net": "2021-09-30T00:00:00Z",
    "window_end": "2021-09-30T00:00:00Z",
    "window_start": "2021-09-30T00:00:00Z",
    "probability": -1,
    "holdreason": "",
    "failreason": "",
    "hashtag": "",
    "launch_service_provider": {
      "id": 184,
      "url": "https://ll.thespacedevs.com/2.2.0/agencies/184/",
      "name": "China Aerospace Science and Industry Corporation",
      "type": "Government"
    },
    "rocket": {
      "id": 2758,
      "configuration": {
        "id": 135,
        "url": "https://ll.thespacedevs.com/2.2.0/config/launcher/135/",
        "name": "Kuaizhou",
        "family": "Kuaizhou",
        "full_name": "Kuaizhou-1A",
        "variant": "1A"
      }
    },
    "mission": {
      "id": 1156,
      "name": "Jilin-1-02D",
      "description": "Jilin-1 is a series of Chinese commercial remote sensing satellites.",
      "launch_designator": "",
      "type": "Earth Science",
      "orbit": ""
    },
    "pad": {
      "id": 71,
      "url": "https://ll.thespacedevs.com/2.2.0/pad/71/",
      "agency_id": "",
      "name": "Unknown Pad",
      "info_url": "",
      "wiki_url": "",
      "map_url": "",
      "latitude": "40.958",
      "longitude": "100.291",
      "location": {
        "id": 17,
        "url": "https://ll.thespacedevs.com/2.2.0/location/17/",
        "name": "Jiuquan, People's Republic of China",
        "country_code": "CHN",
        "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/location_17_20200803142429.jpg",
        "total_launch_count": 146,
        "total_landing_count": 0
      },
      "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/pad_71_20200803143610.jpg",
      "total_launch_count": 26
    },
    "webcast_live": "",
    "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/kuaizhou_image_20191027094423.jpeg",
    "infographic": "",
    "program": []
  },
  {
    "id": "3985e602-f22f-441f-a0b1-a450ea459da9",
    "url": "https://ll.thespacedevs.com/2.2.0/launch/3985e602-f22f-441f-a0b1-a450ea459da9/",
    "slug": "electron-love-at-first-insight",
    "name": "Electron | Love At First Insight",
    "status": {
      "id": 2,
      "name": "To Be Determined",
      "abbrev": "TBD",
      "description": "Current date is a 'No Earlier Than' estimation based on unreliable or interpreted sources."
    },
    "last_updated": "2021-09-08T20:11:59Z",
    "net": "2021-09-30T00:00:00Z",
    "window_end": "2021-09-30T00:00:00Z",
    "window_start": "2021-09-30T00:00:00Z",
    "probability": "",
    "holdreason": "",
    "failreason": "",
    "hashtag": "",
    "launch_service_provider": {
      "id": 147,
      "url": "https://ll.thespacedevs.com/2.2.0/agencies/147/",
      "name": "Rocket Lab Ltd",
      "type": "Commercial"
    },
    "rocket": {
      "id": 2993,
      "configuration": {
        "id": 26,
        "url": "https://ll.thespacedevs.com/2.2.0/config/launcher/26/",
        "name": "Electron",
        "family": "Electron",
        "full_name": "Electron",
        "variant": ""
      }
    },
    "mission": {
      "id": 1418,
      "name": "Love At First Insight",
      "description": "Payload consists of two BlackSky Gen-2 high-resolution multi-spectral Earth observation satellites.",
      "launch_designator": "",
      "type": "Earth Science",
      "orbit": {
        "id": 17,
        "name": "Sun-Synchronous Orbit",
        "abbrev": "SSO"
      }
    },
    "pad": {
      "id": 65,
      "url": "https://ll.thespacedevs.com/2.2.0/pad/65/",
      "agency_id": 147,
      "name": "Rocket Lab Launch Complex 1A",
      "info_url": "",
      "wiki_url": "https://en.wikipedia.org/wiki/Rocket_Lab_Launch_Complex_1",
      "map_url": "https://www.google.com/maps/place/-39.262833,177.864469",
      "latitude": "-39.262833",
      "longitude": "177.864469",
      "location": {
        "id": 10,
        "url": "https://ll.thespacedevs.com/2.2.0/location/10/",
        "name": "Onenui Station, Mahia Peninsula, New Zealand",
        "country_code": "NZL",
        "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/location_10_20200803142509.jpg",
        "total_launch_count": 21,
        "total_landing_count": 2
      },
      "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/pad_65_20200803143549.jpg",
      "total_launch_count": 21
    },
    "webcast_live": "",
    "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/electron_image_20190705175640.jpeg",
    "infographic": "",
    "program": []
  },
  {
    "id": "671b829d-ec26-4b9f-ac13-e50bdc9cca05",
    "url": "https://ll.thespacedevs.com/2.2.0/launch/671b829d-ec26-4b9f-ac13-e50bdc9cca05/",
    "slug": "pslv-eos-4-risat-1a",
    "name": "PSLV  | EOS-4 (RISAT-1A)",
    "status": {
      "id": 2,
      "name": "To Be Determined",
      "abbrev": "TBD",
      "description": "Current date is a 'No Earlier Than' estimation based on unreliable or interpreted sources."
    },
    "last_updated": "2021-06-21T15:50:09Z",
    "net": "2021-09-30T00:00:00Z",
    "window_end": "2021-09-30T00:00:00Z",
    "window_start": "2021-09-30T00:00:00Z",
    "probability": -1,
    "holdreason": "",
    "failreason": "",
    "hashtag": "",
    "launch_service_provider": {
      "id": 31,
      "url": "https://ll.thespacedevs.com/2.2.0/agencies/31/",
      "name": "Indian Space Research Organization",
      "type": "Government"
    },
    "rocket": {
      "id": 2414,
      "configuration": {
        "id": 7,
        "url": "https://ll.thespacedevs.com/2.2.0/config/launcher/7/",
        "name": "PSLV",
        "family": "PSLV",
        "full_name": "PSLV",
        "variant": ""
      }
    },
    "mission": "",
    "pad": {
      "id": 50,
      "url": "https://ll.thespacedevs.com/2.2.0/pad/50/",
      "agency_id": 31,
      "name": "Satish Dhawan Space Centre First Launch Pad",
      "info_url": "",
      "wiki_url": "https://en.wikipedia.org/wiki/Satish_Dhawan_Space_Centre_First_Launch_Pad",
      "map_url": "https://www.google.com/maps?q=13.733,80.235",
      "latitude": "13.733",
      "longitude": "80.235",
      "location": {
        "id": 14,
        "url": "https://ll.thespacedevs.com/2.2.0/location/14/",
        "name": "Sriharikota, Republic of India",
        "country_code": "IND",
        "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/location_14_20200803142403.jpg",
        "total_launch_count": 78,
        "total_landing_count": 0
      },
      "map_image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launch_images/pad_50_20200803143457.jpg",
      "total_launch_count": 50
    },
    "webcast_live": "",
    "image": "https://spacelaunchnow-prod-east.nyc3.digitaloceanspaces.com/media/launcher_images/pslv_image_20190508083736.jpeg",
    "infographic": "",
    "program": []
  }
]
data_format = {
  "launch_name" : "",
  "date_time" : "",
  "current_stage" : "",
  "launch_status" : "",
  "launch_provider" : "",
  "rocket_config" : "",
  "payload_name" : "",
  "payload_mission" : "",
  "location" : "",
}
sorted_data = []


# def get_data():
#   got_data = requests.get('https://ll.thespacedevs.com/2.2.0/launch/upcoming')
#   seed_list = json.loads(got_data.text)
#   print(json.dumps(seed_list['results'], indent = 2))
  

# get_data()  

def sort_data():
  for l in range(len(seed_list)):
    if isinstance(seed_list[l]['mission'], str):
      sorted_data.append({
        "model" : "launches.launch",
        "pk" : f'{l}',
        "fields": {
          "launch_name" : f'{seed_list[l]["name"]}',
          "date_time" : f'window start: {seed_list[l]["window_start"]} window end: {seed_list[l]["window_end"]}  ',
          "current_stage" : "",
          "launch_status" : f'status: {seed_list[l]["status"]["name"]} reason: {seed_list[l]["status"]["description"]}',
          "launch_provider" : f'{seed_list[l]["launch_service_provider"]["name"]}',
          "rocket_config" : f'{seed_list[l]["rocket"]["configuration"]["name"]}',
          "payload_name" : "unknown",
          "payload_mission" : "unknown",
          "location" : f'{seed_list[l]["pad"]["longitude"]} {seed_list[l]["pad"]["latitude"]}',
        }
      })
    else:
      sorted_data.append({
        "model" : "launches.launch",
        "pk" : f'{l}',
        "fields": {
          "launch_name" : f'{seed_list[l]["name"]}',
          "date_time" : f'window start: {seed_list[l]["window_start"]} window end: {seed_list[l]["window_end"]}  ',
          "current_stage" : "",
          "launch_status" : f'status: {seed_list[l]["status"]["name"]} reason: {seed_list[l]["status"]["description"]}',
          "launch_provider" : f'{seed_list[l]["launch_service_provider"]["name"]}',
          "rocket_config" : f'{seed_list[l]["rocket"]["configuration"]["name"]}',
          "payload_name" : f'{seed_list[l]["mission"]["name"]}',
          "payload_mission" : f'{seed_list[l]["mission"]["description"]}',
          "location" : f'{seed_list[l]["pad"]["longitude"]} {seed_list[l]["pad"]["latitude"]}',
        }  
      })
  print(json.dumps(sorted_data, sort_keys=False, indent=4))

sort_data()
