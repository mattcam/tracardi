from tracardi.domain.system_entity_table_column import SystemEntityTableColumn

default_profile_table_columns = [
    SystemEntityTableColumn(
        id="id",
        database="tracardi",
        table="profile",
        type="string",
        default=None,
        nullable=False
    ),

    SystemEntityTableColumn(
        id="ids",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="metadata_time_insert",
        database="tracardi",
        table="profile",
        type="datetime",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="metadata_time_create",
        database="tracardi",
        table="profile",
        type="datetime",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="metadata_time_update",
        database="tracardi",
        table="profile",
        type="datetime",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="operation_new",
        database="tracardi",
        table="profile",
        type="bool",
        default="False",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="operation_update",
        database="tracardi",
        table="profile",
        type="bool",
        default="False",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="stats_visits",
        database="tracardi",
        table="profile",
        type="integer",
        default="0",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="stats_views",
        database="tracardi",
        table="profile",
        type="integer",
        default="0",
        nullable=False
    ),

    SystemEntityTableColumn(
        id="stats_counters",
        database="tracardi",
        table="profile",
        type="dict",
        default="{}",
        nullable=False
    ),

    SystemEntityTableColumn(
        id="traits",
        database="tracardi",
        table="profile",
        type="dict",
        default="{}",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="segments",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="interests",
        database="tracardi",
        table="profile",
        type="dict",
        default="{}",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="consents",
        database="tracardi",
        table="profile",
        type="Dict[str, ConsentRevoke]",
        default="{}",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="active",
        database="tracardi",
        table="profile",
        type="bool",
        default="True",
        nullable=False
    ),

    SystemEntityTableColumn(
        id="aux",
        database="tracardi",
        table="profile",
        type="dict",
        default="{}",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_anonymous",
        database="tracardi",
        table="profile",
        type="bool",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_firstname",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_lastname",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_display_name",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_birthday",
        database="tracardi",
        table="profile",
        type="datetime",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_language_native",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_language_spoken",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_gender",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_education_level",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_civil_status",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_attributes_height",
        database="tracardi",
        table="profile",
        type="float",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_attributes_weight",
        database="tracardi",
        table="profile",
        type="float",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_pii_attributes_shoe_number",
        database="tracardi",
        table="profile",
        type="float",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_email_main",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_email_private",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_email_business",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_phone_main",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_phone_business",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_phone_mobile",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_phone_whatsapp",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_app_whatsapp",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_app_discord",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_app_slack",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_app_twitter",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_app_telegram",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_app_wechat",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_app_viber",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_app_signal",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_address_town",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_address_county",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_address_country",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_address_postcode",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_address_street",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_address_other",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_identifier_id",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_identifier_pk",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_identifier_badge",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_identifier_passport",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_identifier_credit_card",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_identifier_token",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_identifier_coupons",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_media_image",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_media_webpage",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_media_social_twitter",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_media_social_facebook",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_media_social_youtube",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_media_social_instagram",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_media_social_tiktok",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_media_social_linkedin",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_media_social_reddit",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_media_social_other",
        database="tracardi",
        table="profile",
        type="dict",
        default="{}",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_preferences_purchases",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_preferences_colors",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_preferences_sizes",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_preferences_devices",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_preferences_channels",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_preferences_payments",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_preferences_brands",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_preferences_fragrances",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_preferences_services",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_preferences_other",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_job_position",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_job_salary",
        database="tracardi",
        table="profile",
        type="float",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_job_type",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_job_company_name",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_job_company_size",
        database="tracardi",
        table="profile",
        type="int",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_job_company_segment",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_job_company_country",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_job_department",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_metrics_ltv",
        database="tracardi",
        table="profile",
        type="float",
        default="0",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_loyalty_codes",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_loyalty_card_id",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_loyalty_card_name",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_loyalty_card_issuer",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_loyalty_card_expires",
        database="tracardi",
        table="profile",
        type="datetime",
        default="NULL",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_loyalty_card_points",
        database="tracardi",
        table="profile",
        type="float",
        default="0",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_devices_push",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_devices_other",
        database="tracardi",
        table="profile",
        type="List[str]",
        default="[]",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_devices_last_geo_location",
        database="tracardi",
        table="profile",
        type="Tuple[float,float]",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_devices_last_geo_longitude",
        database="tracardi",
        table="profile",
        type="float",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_devices_last_geo_latitude",
        database="tracardi",
        table="profile",
        type="float",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_devices_last_geo_postal",
        database="tracardi",
        table="profile",
        type="string",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_devices_last_geo_county",
        database="tracardi",
        table="profile",
        type="string",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_devices_last_geo_city",
        database="tracardi",
        table="profile",
        type="string",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_devices_last_geo_country_code",
        database="tracardi",
        table="profile",
        type="string",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_devices_last_geo_country_name",
        database="tracardi",
        table="profile",
        type="string",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="data_contact_confirmations",
        database="tracardi",
        table="profile",
        type="List[str]",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="stats_views",
        database="tracardi",
        table="profile",
        type="integer",
        default="0",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="stats_visits",
        database="tracardi",
        table="profile",
        type="integer",
        default="0",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="operation_merge",
        database="tracardi",
        table="profile",
        type="List[str]",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="operation_segment",
        database="tracardi",
        table="profile",
        type="bool",
        default="false",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="metadata_status",
        database="tracardi",
        table="profile",
        type="string",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="metadata_time_visit_tz",
        database="tracardi",
        table="profile",
        type="string",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="metadata_time_visit_count",
        database="tracardi",
        table="profile",
        type="integer",
        default="0",
        nullable=True
    ),

    SystemEntityTableColumn(
        id="metadata_time_visit_current",
        database="tracardi",
        table="profile",
        type="datetime",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="metadata_time_visit_last",
        database="tracardi",
        table="profile",
        type="datetime",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="metadata_time_segmentation",
        database="tracardi",
        table="profile",
        type="datetime",
        default=None,
        nullable=True
    ),

    SystemEntityTableColumn(
        id="primary_id",
        database="tracardi",
        table="profile",
        type="string",
        default="NULL",
        nullable=True
    ),
]
