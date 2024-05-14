from tracardi.domain.system_entity_mapping import SystemEntityPropertyToColumn

profile_properties_to_column_mapping = [
    SystemEntityPropertyToColumn(
        id="70559907-822f-4598-86ba-475c8799ab81",
        property_id="48be9511-7873-4e5a-aae1-cf62216e43c5",  # id
        column_id="e63f494d-9db2-4a8e-aedd-4b0a939e270f",  # id
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="b2d49f48-3fb1-4dbd-b6bb-640408e3e076",
        property_id="48be9511-7873-4e5a-aae1-cf62216e43c5",  # id
        column_id="e63f494d-9db2-4a8e-aedd-4b0a939e270f",  # id
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="b2db4b5a-104f-4cda-9d93-2a9f7e6486a6",
        property_id="90b98e78-fb16-45ba-8691-081e06d1ca2b",  # ids
        column_id="1a4d727d-dc24-450f-bbe8-c32a89c6719a",  # ids
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="949a44e2-263f-4645-bb8d-7a6e1be79a0a",
        property_id="90b98e78-fb16-45ba-8691-081e06d1ca2b",  # ids
        column_id="1a4d727d-dc24-450f-bbe8-c32a89c6719a",  # ids
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="e32f646e-2c81-441a-8475-9eb6fe2efb0a",
        property_id="72da7d73-d22b-4dfa-bb54-cec669292e1f",  # metadata.time.insert
        column_id="c779481e-299b-4333-b1ec-74e379b22684",  # metadata_time_insert
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="1cf2ed3f-a971-4c9a-aec4-aad0b960d738",
        property_id="72da7d73-d22b-4dfa-bb54-cec669292e1f",  # metadata.time.insert
        column_id="c779481e-299b-4333-b1ec-74e379b22684",  # metadata_time_insert
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="a833d416-c88f-4c13-885f-15305bfeddca",
        property_id="80d5979a-7bb5-4768-9a79-02dc3c740244",  # metadata.time.create
        column_id="a785bb0f-215d-4d93-8fab-007f8ec7ec58",  # metadata_time_create
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="ccc066a2-9f18-46bc-8e41-cbaea761baf2",
        property_id="80d5979a-7bb5-4768-9a79-02dc3c740244",  # metadata.time.create
        column_id="a785bb0f-215d-4d93-8fab-007f8ec7ec58",  # metadata_time_create
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="42cc5d8e-f542-4b22-b952-ac0e2b4c7982",
        property_id="19ae8b3a-ef2e-4347-ba99-0b0e1c81f80d",  # metadata.time.update
        column_id="124ecf3b-b30e-40a5-9e3f-a6cadf4dcb21",  # metadata_time_update
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="305d77bb-ac0d-4af7-95be-b0b91fa84017",
        property_id="19ae8b3a-ef2e-4347-ba99-0b0e1c81f80d",  # metadata.time.update
        column_id="124ecf3b-b30e-40a5-9e3f-a6cadf4dcb21",  # metadata_time_update
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="9044b0f8-9848-4f73-bf34-ebdded5fe740",
        property_id="d20af14d-bb6f-44b8-a41f-040aca7842fc",  # operation.new
        column_id="39a27a6c-82bd-4352-a623-2a65b0cdd4b0",  # operation_new
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="2298617a-cb8e-4a9d-aafd-6a8dcc350f02",
        property_id="d20af14d-bb6f-44b8-a41f-040aca7842fc",  # operation.new
        column_id="39a27a6c-82bd-4352-a623-2a65b0cdd4b0",  # operation_new
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="5547da98-c3dc-4042-9688-cd8405babc12",
        property_id="16511736-2413-4f5a-9c5c-7db6ad8aa390",  # operation.update
        column_id="27b5df99-84b6-43e5-a13c-9f57159c4f71",  # operation_update
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="172c4fb6-f8d5-4ec0-99a8-72289210380d",
        property_id="16511736-2413-4f5a-9c5c-7db6ad8aa390",  # operation.update
        column_id="27b5df99-84b6-43e5-a13c-9f57159c4f71",  # operation_update
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="8203bbce-2dde-41b3-8c37-80762cc0af3c",
        property_id="cec510f0-d4e9-4061-bb21-e92aaa8f10cd",  # stats.visits
        column_id="930a5e7c-1315-4c25-9e3a-e46fcdd034b5",  # stats_visits
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="8ea21478-c9e7-4faa-b426-57a49987388b",
        property_id="cec510f0-d4e9-4061-bb21-e92aaa8f10cd",  # stats.visits
        column_id="930a5e7c-1315-4c25-9e3a-e46fcdd034b5",  # stats_visits
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="8d2be422-f944-4dc9-9c08-27c68a7dee34",
        property_id="68be2a45-f71e-4416-923e-2544f6af727d",  # stats.views
        column_id="c5d9acb2-f16c-4b64-b691-6a9cbf4f9f91",  # stats_views
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="157a4794-43c7-4360-aba9-606fe8ea3253",
        property_id="68be2a45-f71e-4416-923e-2544f6af727d",  # stats.views
        column_id="c5d9acb2-f16c-4b64-b691-6a9cbf4f9f91",  # stats_views
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="b8c6ff2b-91ca-429a-b8a2-0bbe2f90c90c",
        property_id="4e2606f4-06a4-4449-8335-4290042835a6",  # stats.counters
        column_id="1aac4e3a-59d6-4e48-8b86-efd36cfd0992",  # stats_counters
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="da9df33a-4818-4f73-af2e-fc3059a98480",
        property_id="4e2606f4-06a4-4449-8335-4290042835a6",  # stats.counters
        column_id="1aac4e3a-59d6-4e48-8b86-efd36cfd0992",  # stats_counters
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="50f5e633-be59-4ff2-b1df-409f2bfbef1d",
        property_id="d28cd5bb-6390-4b41-97b4-d0d1818c1e75",  # traits
        column_id="7f2ef0ea-3543-47e6-93f4-41b47836bed6",  # traits
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="1eedc36a-fb43-45c4-ac0c-6cc9b26c015a",
        property_id="d28cd5bb-6390-4b41-97b4-d0d1818c1e75",  # traits
        column_id="7f2ef0ea-3543-47e6-93f4-41b47836bed6",  # traits
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="2fab0601-da90-4efc-af40-883b36a14fd2",
        property_id="73bc2894-0164-40b0-9684-8492c1ab31ae",  # segments
        column_id="84c52865-c268-4996-922d-09b8dea698d3",  # segments
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="d536d5b6-5a45-4fe2-917a-65c28a0dafb6",
        property_id="73bc2894-0164-40b0-9684-8492c1ab31ae",  # segments
        column_id="84c52865-c268-4996-922d-09b8dea698d3",  # segments
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="d8a9624d-ab82-4a44-904a-7a3289aea822",
        property_id="4b7c196a-d546-4e82-b74a-7d4e0fe41ab1",  # interests
        column_id="631d7f8d-3e3e-4c6e-8ea4-c57ff851796a",  # interests
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="3be3b658-b75a-48d3-8cf0-8513c11483fe",
        property_id="4b7c196a-d546-4e82-b74a-7d4e0fe41ab1",  # interests
        column_id="631d7f8d-3e3e-4c6e-8ea4-c57ff851796a",  # interests
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="2c7f48e5-8cc1-410f-9be6-56bd1c0f8e1d",
        property_id="ae3c5af2-9a38-4bd6-b89f-7cd242262edb",  # consents
        column_id="8ad98361-58a0-426c-b502-b0d88ba5a51d",  # consents
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="8018b353-75c3-4ffa-a4fb-ef9baad29eef",
        property_id="ae3c5af2-9a38-4bd6-b89f-7cd242262edb",  # consents
        column_id="8ad98361-58a0-426c-b502-b0d88ba5a51d",  # consents
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="f262e06c-f318-42e3-8c00-75af6d6321db",
        property_id="72144715-de3b-4a2f-915b-77d745d73d7c",  # active
        column_id="9ced8bb6-62db-4464-9e88-682b45169306",  # active
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="e8608d22-3e25-44d8-a468-1fcb3a9858f3",
        property_id="72144715-de3b-4a2f-915b-77d745d73d7c",  # active
        column_id="9ced8bb6-62db-4464-9e88-682b45169306",  # active
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="f5fdc69c-1dc0-4893-956f-6d53c5206fdb",
        property_id="ef46fe0a-7f24-4757-a0e4-4dd23c432467",  # aux
        column_id="1f1376eb-9f93-405a-87bf-3802b995acc8",  # aux
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="bfccf693-4329-4e06-b909-22e84067c2de",
        property_id="ef46fe0a-7f24-4757-a0e4-4dd23c432467",  # aux
        column_id="1f1376eb-9f93-405a-87bf-3802b995acc8",  # aux
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="190dead1-3f8e-4fb3-a350-7d3a53d0b9d2",
        property_id="385e06a8-9204-4c72-8e45-bd12369d389c",  # data.anonymous
        column_id="20467887-3027-4c77-9cf1-e33a001dcada",  # data_anonymous
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="137c9804-9265-4c42-a5e2-3d085d4f9039",
        property_id="385e06a8-9204-4c72-8e45-bd12369d389c",  # data.anonymous
        column_id="20467887-3027-4c77-9cf1-e33a001dcada",  # data_anonymous
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="ab2c8c5e-7a24-4fda-a901-9b19d08c3cf5",
        property_id="ad6d03af-c223-48f4-b675-650949d8d484",  # data.pii.firstname
        column_id="994cb5b7-08de-4159-8ee1-9b2f05afff02",  # data_pii_firstname
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="5dd439a7-a5f6-41ac-8699-f7960f45c62b",
        property_id="ad6d03af-c223-48f4-b675-650949d8d484",  # data.pii.firstname
        column_id="994cb5b7-08de-4159-8ee1-9b2f05afff02",  # data_pii_firstname
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="6c68666b-04a3-4ed7-b809-b5c14beee72c",
        property_id="1da7eecd-9938-4f8e-9329-d2e50524c621",  # data.pii.lastname
        column_id="5cf6e8c5-9151-4dfd-ba11-0b36005d9f10",  # data_pii_lastname
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="1e9db62f-d715-4d04-90ca-4360f1187725",
        property_id="1da7eecd-9938-4f8e-9329-d2e50524c621",  # data.pii.lastname
        column_id="5cf6e8c5-9151-4dfd-ba11-0b36005d9f10",  # data_pii_lastname
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="7bfee41b-db63-4856-9f5c-38a73a3f6239",
        property_id="c013d36a-0a56-4ee9-9956-1a9d9b160946",  # data.pii.display.name
        column_id="ceb3a38f-ebf6-49f6-9174-5583e3cbeffd",  # data_pii_display_name
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="fbccd215-9f02-4ce3-9d69-4d017b5437bd",
        property_id="c013d36a-0a56-4ee9-9956-1a9d9b160946",  # data.pii.display.name
        column_id="ceb3a38f-ebf6-49f6-9174-5583e3cbeffd",  # data_pii_display_name
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="f209c11e-e7ce-4bc0-b121-5acef4e4283b",
        property_id="e81247b4-ae65-4213-86ee-23159ec1a8f3",  # data.pii.birthday
        column_id="fc05a5b4-966c-428c-af1f-27bee80bcdc0",  # data_pii_birthday
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="c25a3166-7c40-49b8-9ac0-3eac3ef9c673",
        property_id="e81247b4-ae65-4213-86ee-23159ec1a8f3",  # data.pii.birthday
        column_id="fc05a5b4-966c-428c-af1f-27bee80bcdc0",  # data_pii_birthday
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="4f0413bc-e60a-497e-b8cb-d9b44d98f240",
        property_id="5e5acb0a-66d7-4c64-ae63-183f0c716368",  # data.pii.language.native
        column_id="3c732205-beb3-449b-944e-dc8e2f3ec81c",  # data_pii_language_native
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="9970748a-bfdb-4f8d-bc80-40876549189a",
        property_id="5e5acb0a-66d7-4c64-ae63-183f0c716368",  # data.pii.language.native
        column_id="3c732205-beb3-449b-944e-dc8e2f3ec81c",  # data_pii_language_native
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="c6a77fcb-06e6-43e3-904f-edb96e2ffbfc",
        property_id="fb0606ed-f5e5-45d7-aeb3-9956b74c35cf",  # data.pii.language.spoken
        column_id="08dcf673-6869-4591-905f-2c92b8b72de7",  # data_pii_language_spoken
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="8764fe0b-af2e-4419-9c5f-886acc0eb613",
        property_id="fb0606ed-f5e5-45d7-aeb3-9956b74c35cf",  # data.pii.language.spoken
        column_id="08dcf673-6869-4591-905f-2c92b8b72de7",  # data_pii_language_spoken
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="00145a8b-265b-4752-85d0-3ee6bf601b0c",
        property_id="a5418ca9-ac17-4bce-84c8-0cc43c51cf00",  # data.pii.gender
        column_id="49226863-5d4e-4b76-9cf0-8f468fb15466",  # data_pii_gender
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="b98f715b-9e39-4796-ae17-8d5e2294825d",
        property_id="a5418ca9-ac17-4bce-84c8-0cc43c51cf00",  # data.pii.gender
        column_id="49226863-5d4e-4b76-9cf0-8f468fb15466",  # data_pii_gender
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="ae470566-17f5-4c64-8260-36f58245263b",
        property_id="64c4a9f8-6118-497e-836a-d29c1d3ee2c7",  # data.pii.education.level
        column_id="52d2e3f8-58ed-4ff5-872c-6c40545e3f1f",  # data_pii_education_level
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="efac7fab-b73f-4849-b01f-7609c29eb435",
        property_id="64c4a9f8-6118-497e-836a-d29c1d3ee2c7",  # data.pii.education.level
        column_id="52d2e3f8-58ed-4ff5-872c-6c40545e3f1f",  # data_pii_education_level
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="0577288d-94fe-4572-ac24-ca657ca1c270",
        property_id="56053f73-23a5-4282-89bf-8f444e6b85f0",  # data.pii.civil.status
        column_id="b003f89d-b1d5-46a6-b360-9d0c12c603b5",  # data_pii_civil_status
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="7a636cb9-bb78-4b34-a51f-66aec13b762b",
        property_id="56053f73-23a5-4282-89bf-8f444e6b85f0",  # data.pii.civil.status
        column_id="b003f89d-b1d5-46a6-b360-9d0c12c603b5",  # data_pii_civil_status
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="2a30e9a3-ce94-4523-9122-105f427ad866",
        property_id="68d6432e-a2f2-4ccb-b954-eba34cbae7bf",  # data.pii.attributes.height
        column_id="5b94bda6-a6ac-490c-afc1-895d92026140",  # data_pii_attributes_height
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="a1146a90-7656-4b93-8eab-3ae32584d0ec",
        property_id="68d6432e-a2f2-4ccb-b954-eba34cbae7bf",  # data.pii.attributes.height
        column_id="5b94bda6-a6ac-490c-afc1-895d92026140",  # data_pii_attributes_height
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="5af730b1-20bc-49d1-8389-8e98b235fcb7",
        property_id="6b9c4f78-c49f-4fa4-87d2-63591d765a52",  # data.pii.attributes.weight
        column_id="1f9e60e2-47c7-4ab4-a16a-1a32b6864c96",  # data_pii_attributes_weight
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="fe39ace7-9f76-4e35-837a-20e765ff232a",
        property_id="6b9c4f78-c49f-4fa4-87d2-63591d765a52",  # data.pii.attributes.weight
        column_id="1f9e60e2-47c7-4ab4-a16a-1a32b6864c96",  # data_pii_attributes_weight
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="97cac524-28be-4a1d-bf06-cfa3cfb024ee",
        property_id="7121a191-fdcd-4fd0-bf9f-3d9b6cdaead3",  # data.pii.attributes.shoe.number
        column_id="0124a7e1-5d4b-426f-bd50-7a2facc5122d",  # data_pii_attributes_shoe_number
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="ad71513a-aeb7-4964-9f3c-b327962c789a",
        property_id="7121a191-fdcd-4fd0-bf9f-3d9b6cdaead3",  # data.pii.attributes.shoe.number
        column_id="0124a7e1-5d4b-426f-bd50-7a2facc5122d",  # data_pii_attributes_shoe_number
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="7fdc5c68-f5f5-49fe-9ace-21c6a25196c7",
        property_id="6c0dcd60-fde5-4c9e-b68a-e1b1425fc327",  # data.contact.email.main
        column_id="ca9dbcd4-7408-4cca-b229-b0de6732392a",  # data_contact_email_main
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="a01a2b80-c99d-4f2c-8a93-010e8d4e00cf",
        property_id="6c0dcd60-fde5-4c9e-b68a-e1b1425fc327",  # data.contact.email.main
        column_id="ca9dbcd4-7408-4cca-b229-b0de6732392a",  # data_contact_email_main
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="26e23886-0d0c-4484-acef-1999fa4d4969",
        property_id="3a614157-5c60-4cbe-83f9-894b9f29de1f",  # data.contact.email.private
        column_id="836b11ba-ee5e-4bd8-86af-f042b634f18b",  # data_contact_email_private
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="8d223f77-9c61-4193-bc88-7834de81648d",
        property_id="3a614157-5c60-4cbe-83f9-894b9f29de1f",  # data.contact.email.private
        column_id="836b11ba-ee5e-4bd8-86af-f042b634f18b",  # data_contact_email_private
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="7dd9a660-f589-461c-8722-5977558aab02",
        property_id="46b19c1c-07f1-40d7-bf30-0186cb5befb3",  # data.contact.email.business
        column_id="8711a0b1-9cfd-4c25-b52d-54c9ab8d9bc6",  # data_contact_email_business
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="97511e80-be84-4c57-af98-b7ab8388354d",
        property_id="46b19c1c-07f1-40d7-bf30-0186cb5befb3",  # data.contact.email.business
        column_id="8711a0b1-9cfd-4c25-b52d-54c9ab8d9bc6",  # data_contact_email_business
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="5d1aecc2-ec4a-42d2-842b-e404a022f0c1",
        property_id="7dba41ab-0cb8-4d60-969d-21313c37db54",  # data.contact.phone.main
        column_id="83f0e7d9-ab10-4d1f-bce5-7b1ec1bff3df",  # data_contact_phone_main
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="a3e348f9-4e4b-4a9a-9caa-c28d592af3a3",
        property_id="7dba41ab-0cb8-4d60-969d-21313c37db54",  # data.contact.phone.main
        column_id="83f0e7d9-ab10-4d1f-bce5-7b1ec1bff3df",  # data_contact_phone_main
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="e2fd3210-4a8b-4f4f-9786-cf68534f36db",
        property_id="0b15236d-17a8-40c5-9d75-037063cf8f18",  # data.contact.phone.business
        column_id="9e4b455d-b126-4fce-b2d0-880112ebc2ce",  # data_contact_phone_business
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="d46ec32f-2e9f-41f1-9f6d-2c65ded3223e",
        property_id="0b15236d-17a8-40c5-9d75-037063cf8f18",  # data.contact.phone.business
        column_id="9e4b455d-b126-4fce-b2d0-880112ebc2ce",  # data_contact_phone_business
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="83269836-1aa0-4f2c-99e0-d7dd48013151",
        property_id="974a233f-eb77-4ca5-86d0-f25b2ac2acaf",  # data.contact.phone.mobile
        column_id="588a8477-5944-4ca3-908b-2b37b0d2a114",  # data_contact_phone_mobile
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="d2c2037f-030e-4e5a-ac43-a7e3d8721a10",
        property_id="974a233f-eb77-4ca5-86d0-f25b2ac2acaf",  # data.contact.phone.mobile
        column_id="588a8477-5944-4ca3-908b-2b37b0d2a114",  # data_contact_phone_mobile
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="ec6b0ae7-e85c-4692-b66a-42c5457a29ef",
        property_id="46be4d30-1483-49e7-b0df-063e5f3117a9",  # data.contact.phone.whatsapp
        column_id="4dfe2cd2-e0f2-48bd-b978-17fbb95ed9fa",  # data_contact_phone_whatsapp
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="092b42bf-85b7-47ba-bfa2-5e4c2348ae8d",
        property_id="46be4d30-1483-49e7-b0df-063e5f3117a9",  # data.contact.phone.whatsapp
        column_id="4dfe2cd2-e0f2-48bd-b978-17fbb95ed9fa",  # data_contact_phone_whatsapp
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="c2cee4d0-68f3-420d-a3a9-f0e0adb6538c",
        property_id="16f62299-8bb5-4f1a-843d-d463a6771a5c",  # data.contact.app.whatsapp
        column_id="b8a68f9e-fa43-438b-94ba-481dba43366a",  # data_contact_app_whatsapp
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="c660c4ed-5269-4ef0-bf72-fcfec2ce0538",
        property_id="16f62299-8bb5-4f1a-843d-d463a6771a5c",  # data.contact.app.whatsapp
        column_id="b8a68f9e-fa43-438b-94ba-481dba43366a",  # data_contact_app_whatsapp
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="9f2b13c2-54eb-491f-af99-f1e0f5124731",
        property_id="e0a5641f-7e90-406d-8284-cf43c80c2e2c",  # data.contact.app.discord
        column_id="9a6f7ec9-1c4a-4478-9bd1-30a588982fda",  # data_contact_app_discord
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="6188a6c7-07bd-4bf2-87f0-15149ffe084c",
        property_id="e0a5641f-7e90-406d-8284-cf43c80c2e2c",  # data.contact.app.discord
        column_id="9a6f7ec9-1c4a-4478-9bd1-30a588982fda",  # data_contact_app_discord
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="d9d09697-2bae-4806-aefd-4c4908bc2e49",
        property_id="800c472c-9133-4f86-ace8-b970a5758d50",  # data.contact.app.slack
        column_id="6ef9658d-ec45-45d3-b9d4-682f6aa7e198",  # data_contact_app_slack
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="55da4b64-0e25-4f6f-80f5-94bb0b9fbb62",
        property_id="800c472c-9133-4f86-ace8-b970a5758d50",  # data.contact.app.slack
        column_id="6ef9658d-ec45-45d3-b9d4-682f6aa7e198",  # data_contact_app_slack
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="9c04adc2-0545-4156-961c-88bd8732ec05",
        property_id="531518e8-92bc-42b3-a661-fa0dea72a8c5",  # data.contact.app.twitter
        column_id="ca931c5e-d0f2-4bc4-afc4-a80e6ff4bab1",  # data_contact_app_twitter
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="d307b9ee-4b65-49a7-b40f-5068be7a5ad1",
        property_id="531518e8-92bc-42b3-a661-fa0dea72a8c5",  # data.contact.app.twitter
        column_id="ca931c5e-d0f2-4bc4-afc4-a80e6ff4bab1",  # data_contact_app_twitter
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="5177e969-5f53-4b9a-b0c8-3e7211db5f74",
        property_id="5f3f80bf-5d07-454a-8d53-17efced18906",  # data.contact.app.telegram
        column_id="ec155c9a-07cc-45a5-98a4-15f973f16250",  # data_contact_app_telegram
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="86d6daea-098a-4feb-80c6-5d9a92fcb69f",
        property_id="5f3f80bf-5d07-454a-8d53-17efced18906",  # data.contact.app.telegram
        column_id="ec155c9a-07cc-45a5-98a4-15f973f16250",  # data_contact_app_telegram
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="9b5a2c88-ebd9-4176-964a-a2bda8172b2d",
        property_id="28c5a0cf-b818-440f-8d78-17f53ff8ce25",  # data.contact.app.wechat
        column_id="93d37ca1-25d6-41d7-afc1-8ba61876e178",  # data_contact_app_wechat
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="d52a8f77-bd30-4476-9423-ff4b280fdfbf",
        property_id="28c5a0cf-b818-440f-8d78-17f53ff8ce25",  # data.contact.app.wechat
        column_id="93d37ca1-25d6-41d7-afc1-8ba61876e178",  # data_contact_app_wechat
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="c03f3605-0016-45f9-a2ef-b1eac12d8c05",
        property_id="29a3a66a-a88b-41d3-a304-2c3bf6d04d56",  # data.contact.app.viber
        column_id="310b570b-b793-4dcd-9399-8c50710a5ba4",  # data_contact_app_viber
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="068a2f44-da84-4870-9095-316286c22bf2",
        property_id="29a3a66a-a88b-41d3-a304-2c3bf6d04d56",  # data.contact.app.viber
        column_id="310b570b-b793-4dcd-9399-8c50710a5ba4",  # data_contact_app_viber
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="29e4b534-4bc3-4e34-abe9-3ff6c8815bf0",
        property_id="93f4e2c7-8f65-41b4-afea-65d5bc05652f",  # data.contact.app.signal
        column_id="99aa5aea-ee4f-498b-936e-b1ef77a0ac52",  # data_contact_app_signal
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="cb247404-cf59-4ccf-9bb4-c13d69d6966a",
        property_id="93f4e2c7-8f65-41b4-afea-65d5bc05652f",  # data.contact.app.signal
        column_id="99aa5aea-ee4f-498b-936e-b1ef77a0ac52",  # data_contact_app_signal
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="f290725f-68db-470e-a6fc-eaee8a853d1b",
        property_id="560c5a1f-25e4-4e6b-b8a8-9a7050ceba55",  # data.contact.address.town
        column_id="2c6c592b-e7c3-411c-a141-dba896fcf41c",  # data_contact_address_town
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="f0ae930d-2fb8-4a99-bb0f-d2a050b4b341",
        property_id="560c5a1f-25e4-4e6b-b8a8-9a7050ceba55",  # data.contact.address.town
        column_id="2c6c592b-e7c3-411c-a141-dba896fcf41c",  # data_contact_address_town
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="668a6cca-4797-4821-960f-1ea99c85d947",
        property_id="eac3170e-7e0a-473c-b4d5-2657fe65f5f5",  # data.contact.address.county
        column_id="7bd11a47-94ac-4a8b-be7d-9974e6cd75ba",  # data_contact_address_county
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="f97d1efe-95fe-4a3c-b6f9-1afee98f5d5d",
        property_id="eac3170e-7e0a-473c-b4d5-2657fe65f5f5",  # data.contact.address.county
        column_id="7bd11a47-94ac-4a8b-be7d-9974e6cd75ba",  # data_contact_address_county
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="895adcae-81d9-4da0-a602-f14f615746b7",
        property_id="6eedc4fc-72e7-44dd-80b6-df2233858f07",  # data.contact.address.country
        column_id="91518bdc-4cf2-4c2d-bb6f-5a0e28781d82",  # data_contact_address_country
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="cd510793-394e-494e-8211-e128b95b9d98",
        property_id="6eedc4fc-72e7-44dd-80b6-df2233858f07",  # data.contact.address.country
        column_id="91518bdc-4cf2-4c2d-bb6f-5a0e28781d82",  # data_contact_address_country
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="e53f06aa-a254-41cc-ad94-974bf0b00112",
        property_id="69a1e665-c472-47ee-8e48-f3dc9ea91cfe",  # data.contact.address.postcode
        column_id="8d55216d-ca66-43ef-a494-a68d456cfdb3",  # data_contact_address_postcode
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="61403e54-52ce-4fa5-9b31-fb2bf890f714",
        property_id="69a1e665-c472-47ee-8e48-f3dc9ea91cfe",  # data.contact.address.postcode
        column_id="8d55216d-ca66-43ef-a494-a68d456cfdb3",  # data_contact_address_postcode
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="53741b95-6a49-410b-875c-9c72daf6c902",
        property_id="56e7371a-f07a-46b9-abf7-568052a1773d",  # data.contact.address.street
        column_id="942b46a6-43c5-4a26-9146-b1a0d43115d6",  # data_contact_address_street
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="dfa78348-86a6-4aca-b7ae-f16458f5e712",
        property_id="56e7371a-f07a-46b9-abf7-568052a1773d",  # data.contact.address.street
        column_id="942b46a6-43c5-4a26-9146-b1a0d43115d6",  # data_contact_address_street
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="aa32cdaa-7701-4b73-b306-489a8c258dcf",
        property_id="6af97951-54f8-4e5c-a619-d44a3acb7b38",  # data.contact.address.other
        column_id="cf6f2082-c64c-425c-a10b-8626fc4d13ab",  # data_contact_address_other
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="283af261-0039-430c-917a-ba7017a3dbc1",
        property_id="6af97951-54f8-4e5c-a619-d44a3acb7b38",  # data.contact.address.other
        column_id="cf6f2082-c64c-425c-a10b-8626fc4d13ab",  # data_contact_address_other
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="2768cbb9-f5c8-4295-9feb-d13851daa93f",
        property_id="bccfcc23-c817-47ac-8f82-13c8096fd82c",  # data.identifier.id
        column_id="95052724-279c-457c-8cc0-040aa2090168",  # data_identifier_id
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="073d5ee6-bc97-4f05-b987-74a38587ed58",
        property_id="bccfcc23-c817-47ac-8f82-13c8096fd82c",  # data.identifier.id
        column_id="95052724-279c-457c-8cc0-040aa2090168",  # data_identifier_id
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="c872151a-a236-4d6a-bd1c-4c267af31a6b",
        property_id="eda6f0c7-ebbc-4f41-963d-a98aaf4ed01c",  # data.identifier.pk
        column_id="2c8d058a-7cb3-431b-95dd-ca5f59ae551a",  # data_identifier_pk
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="6e0ff7a7-b915-4087-86be-93aa43ea4614",
        property_id="eda6f0c7-ebbc-4f41-963d-a98aaf4ed01c",  # data.identifier.pk
        column_id="2c8d058a-7cb3-431b-95dd-ca5f59ae551a",  # data_identifier_pk
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="b52989b3-b003-48f3-be99-e00d7360456c",
        property_id="4b8f474c-ab5f-4b95-b644-86ff8889423d",  # data.identifier.badge
        column_id="373f0c1d-9fec-429e-8407-658cdd60489d",  # data_identifier_badge
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="75f7f548-cc98-4867-8749-8f31969ad193",
        property_id="4b8f474c-ab5f-4b95-b644-86ff8889423d",  # data.identifier.badge
        column_id="373f0c1d-9fec-429e-8407-658cdd60489d",  # data_identifier_badge
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="2b8c2ba5-8a08-4c60-9f7a-08f2a8ac59b8",
        property_id="e769c9b9-ee81-44c7-b8ec-20defefc7478",  # data.identifier.passport
        column_id="cfa5d1aa-a3de-4173-ae93-9170ba360837",  # data_identifier_passport
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="bac6bfc9-ddca-437a-92ad-6d9edf21f80d",
        property_id="e769c9b9-ee81-44c7-b8ec-20defefc7478",  # data.identifier.passport
        column_id="cfa5d1aa-a3de-4173-ae93-9170ba360837",  # data_identifier_passport
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="ea443304-ed52-4a9f-b09e-f678ef85dd9d",
        property_id="5b794097-e360-4023-b272-8d48e64a34cb",  # data.identifier.credit.card
        column_id="c802fe96-2934-418d-933b-423a9d98dee4",  # data_identifier_credit_card
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="07b74670-4e9d-4a77-976e-8c138c4b9821",
        property_id="5b794097-e360-4023-b272-8d48e64a34cb",  # data.identifier.credit.card
        column_id="c802fe96-2934-418d-933b-423a9d98dee4",  # data_identifier_credit_card
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="c10a10c9-0db1-4331-87dc-b3465270d2de",
        property_id="754b36e3-69ae-4f07-ba54-e3efe9d9e342",  # data.identifier.token
        column_id="509827be-2ff8-43a0-b19c-842726abc437",  # data_identifier_token
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="0dfdc6af-5440-4f35-907f-4aa8b2faa8a9",
        property_id="754b36e3-69ae-4f07-ba54-e3efe9d9e342",  # data.identifier.token
        column_id="509827be-2ff8-43a0-b19c-842726abc437",  # data_identifier_token
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="c78e4ad8-5cd5-49c8-8b52-eeef4552e1d0",
        property_id="6d051b80-347a-447c-be9f-75e878e380c4",  # data.identifier.coupons
        column_id="014c7fe9-127d-47ba-9a0a-70fcf110f65d",  # data_identifier_coupons
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="3c4b75cc-a015-4178-aab4-15e716da11ab",
        property_id="6d051b80-347a-447c-be9f-75e878e380c4",  # data.identifier.coupons
        column_id="014c7fe9-127d-47ba-9a0a-70fcf110f65d",  # data_identifier_coupons
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="c4a5c65f-fce8-42dd-a398-2847a7b38953",
        property_id="5acb73b7-da38-4c9a-b713-bc055be079df",  # data.media.image
        column_id="10aed8f8-6bff-4984-93c6-2930b1e39676",  # data_media_image
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="110a0597-53e3-44f3-ad52-cc7402c88528",
        property_id="5acb73b7-da38-4c9a-b713-bc055be079df",  # data.media.image
        column_id="10aed8f8-6bff-4984-93c6-2930b1e39676",  # data_media_image
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="d24d1788-b02a-4809-b6b8-98602918422a",
        property_id="442ee0ad-93a1-404d-ae9c-5bb0cddc349b",  # data.media.webpage
        column_id="5fe42722-6196-4706-a0a5-2c45269fe77d",  # data_media_webpage
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="fb37e975-641d-497b-bb8a-9687d06c4741",
        property_id="442ee0ad-93a1-404d-ae9c-5bb0cddc349b",  # data.media.webpage
        column_id="5fe42722-6196-4706-a0a5-2c45269fe77d",  # data_media_webpage
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="cdf473c9-be71-4ded-b072-37708efa9171",
        property_id="9ec4a2a1-46b5-4f3e-8165-d23291046c8c",  # data.media.social.twitter
        column_id="a66df419-2cfe-4178-a9db-7256856f28d1",  # data_media_social_twitter
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="a0943300-cdfd-4649-be15-4d02a2c14ae4",
        property_id="9ec4a2a1-46b5-4f3e-8165-d23291046c8c",  # data.media.social.twitter
        column_id="a66df419-2cfe-4178-a9db-7256856f28d1",  # data_media_social_twitter
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="a94f4b34-2d89-4606-8816-176d08864c90",
        property_id="b5ff2867-d8d9-4467-a921-2821ee9adfc0",  # data.media.social.facebook
        column_id="503c7b63-1692-49f3-80ba-e4a0159f5c03",  # data_media_social_facebook
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="5ab9addc-1795-4024-bca2-33e3232f5548",
        property_id="b5ff2867-d8d9-4467-a921-2821ee9adfc0",  # data.media.social.facebook
        column_id="503c7b63-1692-49f3-80ba-e4a0159f5c03",  # data_media_social_facebook
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="ff8568e2-3b86-4c43-8f42-72f03160e643",
        property_id="0e8ae744-a37a-48b7-8fd8-de6f3025beaa",  # data.media.social.youtube
        column_id="1706071d-ed88-4681-87f5-dfc01aac96d3",  # data_media_social_youtube
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="54e00d19-1d8c-4a92-9c96-63c2eaf8bec4",
        property_id="0e8ae744-a37a-48b7-8fd8-de6f3025beaa",  # data.media.social.youtube
        column_id="1706071d-ed88-4681-87f5-dfc01aac96d3",  # data_media_social_youtube
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="7ab46fc0-9cff-4629-ac5c-7daaf24002cc",
        property_id="c3d02ec0-f8ff-434e-96cb-97539b07d8af",  # data.media.social.instagram
        column_id="d1c05ad6-db6c-4fb2-a23d-692e40884218",  # data_media_social_instagram
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="c6d9ce30-8c38-48df-97fa-bd1927a7dc94",
        property_id="c3d02ec0-f8ff-434e-96cb-97539b07d8af",  # data.media.social.instagram
        column_id="d1c05ad6-db6c-4fb2-a23d-692e40884218",  # data_media_social_instagram
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="fc03495d-0ceb-4667-a18c-fff8994caaa1",
        property_id="a25673ad-dc68-4a6a-b654-53d15da81046",  # data.media.social.tiktok
        column_id="82428273-765c-4b34-ab47-5e4844018f0a",  # data_media_social_tiktok
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="d8dffdc0-9520-4b96-97b0-5754552beed0",
        property_id="a25673ad-dc68-4a6a-b654-53d15da81046",  # data.media.social.tiktok
        column_id="82428273-765c-4b34-ab47-5e4844018f0a",  # data_media_social_tiktok
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="87c4c995-0c45-4479-a559-a02aedacd432",
        property_id="d8a21e31-3a21-4133-a944-ea028a010477",  # data.media.social.linkedin
        column_id="e03b6a50-8ffc-4ba0-9dde-1492080abbb9",  # data_media_social_linkedin
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="2acfdb1c-143e-4afd-a4ba-452efabb6c2f",
        property_id="d8a21e31-3a21-4133-a944-ea028a010477",  # data.media.social.linkedin
        column_id="e03b6a50-8ffc-4ba0-9dde-1492080abbb9",  # data_media_social_linkedin
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="c49c359a-0d62-496f-a1c6-f33669a7e37e",
        property_id="68715af8-7c05-4b43-b57c-7a449b74c73c",  # data.media.social.reddit
        column_id="9afb81cd-ef4e-4541-ac74-8669f2a66206",  # data_media_social_reddit
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="0c4a04a3-3dfb-41a8-8822-9bb4fd34b434",
        property_id="68715af8-7c05-4b43-b57c-7a449b74c73c",  # data.media.social.reddit
        column_id="9afb81cd-ef4e-4541-ac74-8669f2a66206",  # data_media_social_reddit
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="cc9bc042-982a-42e3-b2aa-ed9d63fa16d4",
        property_id="e7e3c6ca-f61a-4444-949c-6e02b7d3cc31",  # data.media.social.other
        column_id="c830e497-3feb-4de6-8209-a204706d7dcc",  # data_media_social_other
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="3318b404-e63a-48df-a76d-da33c3337044",
        property_id="e7e3c6ca-f61a-4444-949c-6e02b7d3cc31",  # data.media.social.other
        column_id="c830e497-3feb-4de6-8209-a204706d7dcc",  # data_media_social_other
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="bdda29f4-04a8-472b-8b6b-a2f1f979eff5",
        property_id="db1f7f98-30fe-4082-beab-a816a43264f5",  # data.preferences.purchases
        column_id="1bd081aa-c046-430a-b66e-896277107ac3",  # data_preferences_purchases
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="68be94f5-1af8-48c0-a78c-96faed6d4062",
        property_id="db1f7f98-30fe-4082-beab-a816a43264f5",  # data.preferences.purchases
        column_id="1bd081aa-c046-430a-b66e-896277107ac3",  # data_preferences_purchases
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="05e16df9-9b10-442b-a793-bcb1576bacb8",
        property_id="9ba0d923-e040-4a3c-b049-24d503abbbee",  # data.preferences.colors
        column_id="909cef70-7e09-4abc-87ad-50683ff3e2a1",  # data_preferences_colors
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="302f9d10-ad68-419c-ab49-e23b9633d92a",
        property_id="9ba0d923-e040-4a3c-b049-24d503abbbee",  # data.preferences.colors
        column_id="909cef70-7e09-4abc-87ad-50683ff3e2a1",  # data_preferences_colors
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="28ff4551-57f5-4945-bb2c-2097ed27ac27",
        property_id="567e7d26-5be2-43e0-9427-c10bc5f75044",  # data.preferences.sizes
        column_id="cccfe951-2c04-4a0e-9f9d-fe332f54eb5f",  # data_preferences_sizes
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="29b92214-bd4d-4004-936a-7e291239691b",
        property_id="567e7d26-5be2-43e0-9427-c10bc5f75044",  # data.preferences.sizes
        column_id="cccfe951-2c04-4a0e-9f9d-fe332f54eb5f",  # data_preferences_sizes
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="24c8a47c-45c5-4025-9782-ec69c6bbc450",
        property_id="07bab6d0-263c-4999-a5d2-205c88d3daae",  # data.preferences.devices
        column_id="eeeceb92-6fe4-4cd0-b602-39a52860923c",  # data_preferences_devices
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="97b94ca5-326d-498f-8209-df9c6a4ac615",
        property_id="07bab6d0-263c-4999-a5d2-205c88d3daae",  # data.preferences.devices
        column_id="eeeceb92-6fe4-4cd0-b602-39a52860923c",  # data_preferences_devices
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="73f28911-8688-47e7-8e6c-ca32de6746f1",
        property_id="63b9bf46-6ad3-4ac1-ac98-fb0886a38aaa",  # data.preferences.channels
        column_id="b86968fd-9f05-4c03-bab9-71f2948be896",  # data_preferences_channels
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="c7c1d330-4026-4de8-a558-f5ea225636d1",
        property_id="63b9bf46-6ad3-4ac1-ac98-fb0886a38aaa",  # data.preferences.channels
        column_id="b86968fd-9f05-4c03-bab9-71f2948be896",  # data_preferences_channels
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="8676e020-7bde-4914-98b3-098f0f8ccbd3",
        property_id="e96d6dc4-024b-4d44-a8ef-e20a38aed394",  # data.preferences.payments
        column_id="c3036ef6-7b06-42d8-982f-b4dcb1c6dbf8",  # data_preferences_payments
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="7550e116-d07d-4471-b17c-761f31ce366a",
        property_id="e96d6dc4-024b-4d44-a8ef-e20a38aed394",  # data.preferences.payments
        column_id="c3036ef6-7b06-42d8-982f-b4dcb1c6dbf8",  # data_preferences_payments
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="3277fc49-0692-4f9e-ba8d-6bef7fa2f40c",
        property_id="ccc7f7b4-856f-46e3-aacb-d9c8437aa218",  # data.preferences.brands
        column_id="a032bf17-130a-447b-b846-839850fe653e",  # data_preferences_brands
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="4b5916f0-f37e-4be4-83bb-0e71d08bb5f1",
        property_id="ccc7f7b4-856f-46e3-aacb-d9c8437aa218",  # data.preferences.brands
        column_id="a032bf17-130a-447b-b846-839850fe653e",  # data_preferences_brands
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="c304f3c8-1c8b-40f3-8a95-4357cec6e235",
        property_id="d0c96de4-67a7-4cc2-952d-596eede1d695",  # data.preferences.fragrances
        column_id="f9b59277-9bf5-42e7-a8b0-d9e2767aedbf",  # data_preferences_fragrances
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="5601d4fa-9900-4165-bbdd-b62f09ea06b3",
        property_id="d0c96de4-67a7-4cc2-952d-596eede1d695",  # data.preferences.fragrances
        column_id="f9b59277-9bf5-42e7-a8b0-d9e2767aedbf",  # data_preferences_fragrances
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="5b12a74c-092d-4d0d-b83a-ebb428b6a1c0",
        property_id="80181d7d-99e4-4fb7-9c5b-81d537a41390",  # data.preferences.services
        column_id="3f6624db-8481-4ed8-994a-ce75f1b0e291",  # data_preferences_services
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="cb167b67-5b8a-49a0-9425-7c45b33e443f",
        property_id="80181d7d-99e4-4fb7-9c5b-81d537a41390",  # data.preferences.services
        column_id="3f6624db-8481-4ed8-994a-ce75f1b0e291",  # data_preferences_services
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="d706e810-c491-4495-8b51-35e126234508",
        property_id="b58c4484-2900-4de4-9c78-884053c1502e",  # data.preferences.other
        column_id="0d0adda4-8cf6-4f92-80cc-baceb91a7112",  # data_preferences_other
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="14e9cb4a-6bc9-4a45-8071-52774590dfe3",
        property_id="b58c4484-2900-4de4-9c78-884053c1502e",  # data.preferences.other
        column_id="0d0adda4-8cf6-4f92-80cc-baceb91a7112",  # data_preferences_other
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="b4a2ef45-680b-4487-8c12-854b3ca25b11",
        property_id="1dc6070b-cddc-494b-92ba-a1247e3bd0cb",  # data.job.position
        column_id="635660c2-4fcb-41e6-8b14-42cb6c4e8615",  # data_job_position
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="4ca9ac1c-bffd-4e71-b27f-159b7170a8b4",
        property_id="1dc6070b-cddc-494b-92ba-a1247e3bd0cb",  # data.job.position
        column_id="635660c2-4fcb-41e6-8b14-42cb6c4e8615",  # data_job_position
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="8fe79c70-93b0-4024-8705-9dd5ebdf533d",
        property_id="6b1cffb9-9e84-43b2-9dd0-e127bf1af73d",  # data.job.salary
        column_id="f8550a44-cb59-4655-af1c-651675acd6ec",  # data_job_salary
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="136504bf-071b-4749-9f84-16351f1c7e64",
        property_id="6b1cffb9-9e84-43b2-9dd0-e127bf1af73d",  # data.job.salary
        column_id="f8550a44-cb59-4655-af1c-651675acd6ec",  # data_job_salary
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="e05dd893-3493-4a68-b12d-074af7c4e1e3",
        property_id="c2150f5e-99c2-4100-8a8a-4aebb37778ed",  # data.job.type
        column_id="d053d676-96b4-4152-8579-cc071a6e197b",  # data_job_type
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="603aa334-700f-4aa4-932a-1ee2d3d6ec0c",
        property_id="c2150f5e-99c2-4100-8a8a-4aebb37778ed",  # data.job.type
        column_id="d053d676-96b4-4152-8579-cc071a6e197b",  # data_job_type
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="da6246aa-8ea0-440e-b991-907c6a52ebae",
        property_id="3cfd8c36-36e9-4e92-88fd-f332e97e1ee8",  # data.job.company.name
        column_id="aa33bded-78b9-4c2a-94fd-ee8665d6ba10",  # data_job_company_name
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="afd34df7-05f5-4853-9829-b2b63aa0a820",
        property_id="3cfd8c36-36e9-4e92-88fd-f332e97e1ee8",  # data.job.company.name
        column_id="aa33bded-78b9-4c2a-94fd-ee8665d6ba10",  # data_job_company_name
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="69c2ca5e-1fd1-4939-b512-948dd356ce6c",
        property_id="083fafcc-1d30-4101-823e-b744368d48b1",  # data.job.company.size
        column_id="362c3f69-ad22-4c72-aa7c-b42fe52e9820",  # data_job_company_size
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="b92acbc2-c88f-467c-a7f9-a83f37da8dd6",
        property_id="083fafcc-1d30-4101-823e-b744368d48b1",  # data.job.company.size
        column_id="362c3f69-ad22-4c72-aa7c-b42fe52e9820",  # data_job_company_size
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="70492fa3-920a-4fc1-b10e-ba7fba692dfe",
        property_id="7859ff38-c4fd-4dd4-a051-a9ed725bdf38",  # data.job.company.segment
        column_id="1df26195-e779-44bd-8848-76db6fc7dceb",  # data_job_company_segment
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="f6b7b1cc-0e0f-42d1-bcfe-67da08554711",
        property_id="7859ff38-c4fd-4dd4-a051-a9ed725bdf38",  # data.job.company.segment
        column_id="1df26195-e779-44bd-8848-76db6fc7dceb",  # data_job_company_segment
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="563d6cee-f043-4ee0-91cc-9f3220e2b1da",
        property_id="1678886e-c92f-4a31-ac4a-d0f778333df4",  # data.job.company.country
        column_id="c6feb282-5d63-477e-bae9-abb0fa25b96a",  # data_job_company_country
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="1ee57f42-177d-4c99-872c-5f3b64077c0a",
        property_id="1678886e-c92f-4a31-ac4a-d0f778333df4",  # data.job.company.country
        column_id="c6feb282-5d63-477e-bae9-abb0fa25b96a",  # data_job_company_country
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="8b632176-2257-431a-ad11-89c3714b88fe",
        property_id="5b7c5e18-d481-4a7d-8bc7-6552f7b0de35",  # data.job.department
        column_id="864090dc-e468-409d-ae99-38e9a54c1b92",  # data_job_department
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="71368119-798e-47a3-8739-229a057e039e",
        property_id="5b7c5e18-d481-4a7d-8bc7-6552f7b0de35",  # data.job.department
        column_id="864090dc-e468-409d-ae99-38e9a54c1b92",  # data_job_department
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="05d2b4a4-9f47-427f-bf7b-9c01f7e14cde",
        property_id="d986bad5-da8e-4e9d-ad2d-bc17380ff908",  # data.metrics.ltv
        column_id="e5b643a5-4d0b-4615-b6a1-b0b4f0ca0cb5",  # data_metrics_ltv
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="0f1faf66-b5ce-4b8c-b194-a6ede601719c",
        property_id="d986bad5-da8e-4e9d-ad2d-bc17380ff908",  # data.metrics.ltv
        column_id="e5b643a5-4d0b-4615-b6a1-b0b4f0ca0cb5",  # data_metrics_ltv
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="28619d26-c0fe-4f20-8e46-bc6f41d8e3cf",
        property_id="7272384a-765a-4ec7-a92c-8eaa196f0d4c",  # data.loyalty.codes
        column_id="a259b1a2-9bf6-4222-8da0-76a6d86aaf66",  # data_loyalty_codes
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="561ce68f-d6e0-4538-83a8-0c4bf6709788",
        property_id="7272384a-765a-4ec7-a92c-8eaa196f0d4c",  # data.loyalty.codes
        column_id="a259b1a2-9bf6-4222-8da0-76a6d86aaf66",  # data_loyalty_codes
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="3183e390-6a07-445d-8756-f0090ee51734",
        property_id="6b26b032-b96e-4e93-9d79-d693aefba233",  # data.loyalty.card.id
        column_id="a5baab99-e867-4d0f-91fd-3bc190e10dd2",  # data_loyalty_card_id
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="010962e6-99b1-4274-b28d-ed6568d8df21",
        property_id="6b26b032-b96e-4e93-9d79-d693aefba233",  # data.loyalty.card.id
        column_id="a5baab99-e867-4d0f-91fd-3bc190e10dd2",  # data_loyalty_card_id
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="54ecfb9f-69fa-42dc-99e5-5b09e4cbd9c8",
        property_id="a344e194-a984-4a18-8f1a-ba8e9edb0c4e",  # data.loyalty.card.name
        column_id="e7dc4c68-9414-4354-b896-c8edd943cd5d",  # data_loyalty_card_name
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="32ff3b9d-aca5-46fc-bf3b-f24612259cf1",
        property_id="a344e194-a984-4a18-8f1a-ba8e9edb0c4e",  # data.loyalty.card.name
        column_id="e7dc4c68-9414-4354-b896-c8edd943cd5d",  # data_loyalty_card_name
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="2fa96383-bf70-4a52-bc42-f75249460fc8",
        property_id="437b4a1e-ba6a-4795-a2b1-8c9fe9f303bc",  # data.loyalty.card.issuer
        column_id="34c6c658-2dc7-496b-9a22-cb30df46a93d",  # data_loyalty_card_issuer
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="be940d54-f014-4124-863d-4890af7d62f5",
        property_id="437b4a1e-ba6a-4795-a2b1-8c9fe9f303bc",  # data.loyalty.card.issuer
        column_id="34c6c658-2dc7-496b-9a22-cb30df46a93d",  # data_loyalty_card_issuer
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="f346caae-964e-451a-a31f-68f894d3d81f",
        property_id="d55adc4b-028a-413b-b9f4-2ccef49ec277",  # data.loyalty.card.expires
        column_id="ab760f80-6e32-4012-918a-774337196380",  # data_loyalty_card_expires
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="1941c1d5-615e-4303-8710-c4b80bed1042",
        property_id="d55adc4b-028a-413b-b9f4-2ccef49ec277",  # data.loyalty.card.expires
        column_id="ab760f80-6e32-4012-918a-774337196380",  # data_loyalty_card_expires
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="d51c463b-8919-478b-99b2-7f08eb140fee",
        property_id="03421596-29dd-4b6c-9dc5-edb5b4cc5718",  # data.loyalty.card.points
        column_id="73206a75-edd6-442d-9a58-cfbfcdc0da6a",  # data_loyalty_card_points
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="6718a0e6-2bc9-4ed2-b76d-7db496a6a2a0",
        property_id="03421596-29dd-4b6c-9dc5-edb5b4cc5718",  # data.loyalty.card.points
        column_id="73206a75-edd6-442d-9a58-cfbfcdc0da6a",  # data_loyalty_card_points
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="cccc4547-647c-43f8-bf73-e43fc6ac0b37",
        property_id="5979d815-2f76-4753-806b-a4d58de73863",  # data.devices.push
        column_id="6fca8ab4-2471-40df-a12c-6c888a6918df",  # data_devices_push
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="70d1e39b-8678-470a-8c8a-1a2e558092d9",
        property_id="5979d815-2f76-4753-806b-a4d58de73863",  # data.devices.push
        column_id="6fca8ab4-2471-40df-a12c-6c888a6918df",  # data_devices_push
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="7868b68f-a0cb-4301-a6b3-0be9abe4dbd8",
        property_id="d14f5de6-90be-498e-93ed-bf8d63d98ca1",  # data.devices.other
        column_id="bd1a3fb1-34aa-447a-8df6-b64c60171e8f",  # data_devices_other
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="0157a65d-9a16-4d50-ada1-fce7e691d46d",
        property_id="d14f5de6-90be-498e-93ed-bf8d63d98ca1",  # data.devices.other
        column_id="bd1a3fb1-34aa-447a-8df6-b64c60171e8f",  # data_devices_other
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="409da9d0-dd66-4ea2-9506-821a43e27a60",
        property_id="78144375-87ee-49da-bbea-09874c2cd71b",  # data.devices.last.geo.location
        column_id="be8fb25a-9439-41c8-8b0b-36ead967bc76",  # data_devices_last_geo_location
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="3b0a4c75-9ea3-47b4-9555-62de15855a98",
        property_id="78144375-87ee-49da-bbea-09874c2cd71b",  # data.devices.last.geo.location
        column_id="be8fb25a-9439-41c8-8b0b-36ead967bc76",  # data_devices_last_geo_location
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="6ae45938-b7af-4ab3-89f1-f3a109c9227e",
        property_id="3e7aedbd-7597-4897-8b18-3e408f8a917a",  # data.devices.last.geo.longitude
        column_id="74e8e3a6-40cf-46d9-907f-a7e65d9b43e3",  # data_devices_last_geo_longitude
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="654d9b02-9a51-485a-beb9-616b836a0aa1",
        property_id="3e7aedbd-7597-4897-8b18-3e408f8a917a",  # data.devices.last.geo.longitude
        column_id="74e8e3a6-40cf-46d9-907f-a7e65d9b43e3",  # data_devices_last_geo_longitude
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="843d8cf0-6e12-4a74-a6f2-61a941c7b307",
        property_id="cdf12474-d8da-4bfb-b132-78ffcbcc9ab1",  # data.devices.last.geo.latitude
        column_id="cfeff116-cabf-4ff4-9327-15ae3ef67602",  # data_devices_last_geo_latitude
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="b1cea8f5-a6a7-4300-8b4c-94a262b3dc5c",
        property_id="cdf12474-d8da-4bfb-b132-78ffcbcc9ab1",  # data.devices.last.geo.latitude
        column_id="cfeff116-cabf-4ff4-9327-15ae3ef67602",  # data_devices_last_geo_latitude
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="c68422ef-1519-4a40-ae5f-6c2bbe3dfb51",
        property_id="8ed513bf-e2a3-4124-970f-f2287c69fe4d",  # data.devices.last.geo.postal
        column_id="dcf3d7a6-787e-45bb-8f25-2fa5abf55ec7",  # data_devices_last_geo_postal
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="171b3987-1986-41e8-8376-697d141a3036",
        property_id="8ed513bf-e2a3-4124-970f-f2287c69fe4d",  # data.devices.last.geo.postal
        column_id="dcf3d7a6-787e-45bb-8f25-2fa5abf55ec7",  # data_devices_last_geo_postal
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="2bd1e59c-672b-4c2c-b214-e6301c6dce1c",
        property_id="1999c6bd-31fa-4a38-aca3-6e240a148d9b",  # data.devices.last.geo.county
        column_id="d5419a86-fd9a-41b1-8311-0a5799e240cb",  # data_devices_last_geo_county
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="70801b71-6664-4df9-9f6b-72ade3347875",
        property_id="1999c6bd-31fa-4a38-aca3-6e240a148d9b",  # data.devices.last.geo.county
        column_id="d5419a86-fd9a-41b1-8311-0a5799e240cb",  # data_devices_last_geo_county
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="4c8fa742-a4dc-48f3-b397-b0da3bd57f8a",
        property_id="7bfeb655-e063-4cb2-873c-a5ffa3430f2b",  # data.devices.last.geo.city
        column_id="1057c47a-fa1c-4588-a663-9db0a0f91346",  # data_devices_last_geo_city
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="f8079de1-9eff-41ca-abd3-36b3b61e0460",
        property_id="7bfeb655-e063-4cb2-873c-a5ffa3430f2b",  # data.devices.last.geo.city
        column_id="1057c47a-fa1c-4588-a663-9db0a0f91346",  # data_devices_last_geo_city
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="e0198bd1-91be-4773-809d-078db5761e1c",
        property_id="437074e7-0756-45d4-8583-7c6880cf927a",  # data.devices.last.geo.country.code
        column_id="331790a5-b0c6-4fae-a796-72e1dc1b70eb",  # data_devices_last_geo_country_code
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="4538fbe5-8918-4358-bcb9-14895d63afaa",
        property_id="437074e7-0756-45d4-8583-7c6880cf927a",  # data.devices.last.geo.country.code
        column_id="331790a5-b0c6-4fae-a796-72e1dc1b70eb",  # data_devices_last_geo_country_code
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="66f7cef1-ac2b-42e0-90fe-6d8694974951",
        property_id="b1a6b611-f033-4495-8b25-03b2003b587a",  # data.devices.last.geo.country.name
        column_id="a1cdb1d0-c7e3-4023-83ce-8069e6b46569",  # data_devices_last_geo_country_name
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="b8aafcfc-94da-4a34-a243-57e4cfbd0f62",
        property_id="b1a6b611-f033-4495-8b25-03b2003b587a",  # data.devices.last.geo.country.name
        column_id="a1cdb1d0-c7e3-4023-83ce-8069e6b46569",  # data_devices_last_geo_country_name
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="530f1ac6-e2d7-4eb3-b047-4acc0ea2f2dc",
        property_id="6b79adb3-d76b-438c-9bbb-fafca580647b",  # data.contact.confirmations
        column_id="13a3dffe-22d1-4d3a-886d-fb5244a5bfe9",  # data_contact_confirmations
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="50313026-5dd4-4b08-a89c-95d94c822187",
        property_id="6b79adb3-d76b-438c-9bbb-fafca580647b",  # data.contact.confirmations
        column_id="13a3dffe-22d1-4d3a-886d-fb5244a5bfe9",  # data_contact_confirmations
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="5392e318-ef6b-4505-b7d4-278c5b0dfe80",
        property_id="6381ab1f-9b42-4548-9c9e-f1482b40e079",  # operation.merge
        column_id="8a9fcaee-de53-4a1d-9f4d-485e4df0a204",  # operation_merge
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="528e7963-6e83-49b0-915c-a79c5be4d109",
        property_id="6381ab1f-9b42-4548-9c9e-f1482b40e079",  # operation.merge
        column_id="8a9fcaee-de53-4a1d-9f4d-485e4df0a204",  # operation_merge
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="125c35d6-d804-49c9-80be-ccea108a0f3c",
        property_id="a39c5c52-4fe0-4632-bafb-4accdb31313d",  # operation.segment
        column_id="39a9940b-ec54-4552-b7d2-58880af24b12",  # operation_segment
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="902240bc-c1b8-4775-a09d-ffe52e8c4df0",
        property_id="a39c5c52-4fe0-4632-bafb-4accdb31313d",  # operation.segment
        column_id="39a9940b-ec54-4552-b7d2-58880af24b12",  # operation_segment
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="b800d2ac-5693-45f3-8156-99144c40d6eb",
        property_id="e61938e1-21de-46bf-8cfc-f89070e60623",  # metadata.status
        column_id="540d0ed5-8ea0-4595-a998-5757479455d5",  # metadata_status
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="ec22a494-9adb-4cdf-99fe-ea90a53a44d5",
        property_id="e61938e1-21de-46bf-8cfc-f89070e60623",  # metadata.status
        column_id="540d0ed5-8ea0-4595-a998-5757479455d5",  # metadata_status
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="d3df003d-7666-4b55-b0be-55acbdebd789",
        property_id="468e24a2-b314-4476-bbbe-51e816068986",  # metadata.time.visit.tz
        column_id="b27bc369-f1c3-43c6-977e-c4f01656ab77",  # metadata_time_visit_tz
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="beecb75c-2769-4d44-9d53-86b921d2d565",
        property_id="468e24a2-b314-4476-bbbe-51e816068986",  # metadata.time.visit.tz
        column_id="b27bc369-f1c3-43c6-977e-c4f01656ab77",  # metadata_time_visit_tz
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="343978ca-599d-4e83-8349-7652042187a3",
        property_id="e64fe226-ab27-4c8c-9978-9f9f8310a3cd",  # metadata.time.visit.count
        column_id="8e3e72e3-6060-4b53-bc90-2eeeacd039e8",  # metadata_time_visit_count
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="dd22a206-2c30-42a8-81f1-3035f1c25519",
        property_id="e64fe226-ab27-4c8c-9978-9f9f8310a3cd",  # metadata.time.visit.count
        column_id="8e3e72e3-6060-4b53-bc90-2eeeacd039e8",  # metadata_time_visit_count
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="8740a842-f437-4255-947b-59e75865efd3",
        property_id="8f682e20-04ff-48da-9f7c-141c614d9b91",  # metadata.time.visit.current
        column_id="c98a3e81-9caa-469f-ad40-27bd98d0116f",  # metadata_time_visit_current
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="2d00d48b-cae5-44b1-9e0f-03da63e10ea6",
        property_id="8f682e20-04ff-48da-9f7c-141c614d9b91",  # metadata.time.visit.current
        column_id="c98a3e81-9caa-469f-ad40-27bd98d0116f",  # metadata_time_visit_current
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="27a1f775-e8ab-46f9-b4a1-cadde42f7874",
        property_id="61d9747e-090a-4a76-b902-f462230d21a8",  # metadata.time.visit.last
        column_id="739f575d-fdbc-4b28-99af-2aa9ee640f3a",  # metadata_time_visit_last
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="c38d0489-caa7-4708-aca8-c1f4a7c4c8e5",
        property_id="61d9747e-090a-4a76-b902-f462230d21a8",  # metadata.time.visit.last
        column_id="739f575d-fdbc-4b28-99af-2aa9ee640f3a",  # metadata_time_visit_last
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="39ca2e30-78e3-4113-b273-95a838f0c919",
        property_id="d7026962-5828-47a6-9f9d-bb276d80a324",  # metadata.time.segmentation
        column_id="fbd4f752-8deb-425a-9a35-331c9fb2b7eb",  # metadata_time_segmentation
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="96837bfa-a290-4992-8965-4edd212e6caf",
        property_id="d7026962-5828-47a6-9f9d-bb276d80a324",  # metadata.time.segmentation
        column_id="fbd4f752-8deb-425a-9a35-331c9fb2b7eb",  # metadata_time_segmentation
        mode="t"
    ),
    SystemEntityPropertyToColumn(
        id="9ef9db80-dcf1-42a5-b7ab-4f27b98df68d",
        property_id="8b79c364-ab9d-4967-ac90-b98aba0c7ed2",  # primary.id
        column_id="78c40875-cb02-4814-80dd-b662a1922c62",  # primary_id
        mode="p"
    ),
    SystemEntityPropertyToColumn(
        id="23b9de4d-f99c-4443-b877-e1220cee7c3e",
        property_id="8b79c364-ab9d-4967-ac90-b98aba0c7ed2",  # primary.id
        column_id="78c40875-cb02-4814-80dd-b662a1922c62",  # primary_id
        mode="t"
    ),
]
