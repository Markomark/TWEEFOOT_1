DELETE FROM "BASE_TWEETS"  USING "BASE_TWEETS"  alias 
  WHERE "BASE_TWEETS".id = alias.id AND 
    "BASE_TWEETS".retweet_count < alias.retweet_count;
delete from public."BASE_TWEETS" 
    where exists (select 1
                  from "BASE_TWEETS" t2
                  where t2.id = "BASE_TWEETS".id and

                        t2.ctid > "BASE_TWEETS".ctid
                 );		



Drop table public."Mix2" ; 


Create table public."Mix2" as sELECT 
a.index as index_U,
a.follow_request_sent as follow_request_sent_U,
a.has_extended_profile as has_extended_profile_U,
a.profile_use_background_image as profile_use_background_image_U,
a.idd as idd_U,
a.default_profile as default_profile_U,
a.verified as verified_U,
a.profile_text_color as profile_text_color_U,
a.profile_image_url_https as profile_image_url_https_U,
a.profile_sidebar_fill_color as profile_sidebar_fill_color_U,
a.is_translator as is_translator_U,
a.geo_enabled as geo_enabled_U,
a.followers_count as followers_count_U,
a.profile_sidebar_border_color as profile_sidebar_border_color_U,
a.location as location_U,
a.default_profile_image as default_profile_image_U,
a.id_str as id_str_U,
a.is_translation_enabled as is_translation_enabled_U,
a.utc_offset as utc_offset_U,
a.statuses_count as statuses_count_U,
a.description as description_U,
a.friends_count as friends_count_U,
a.profile_link_color as profile_link_color_U,
a.profile_image_url as profile_image_url_U,
a.notifications as notifications_U,
a.profile_background_image_url_https as profile_background_image_url_https_U,
a.profile_background_color as profile_background_color_U,
a.profile_background_image_url as profile_background_image_url_U,
a.name as name_U,
a.lang as lang_U,
a.profile_background_tile as profile_background_tile_U,
a.favourites_count as favourites_count_U,
a.screen_name as screen_name_U,
a.url as url_U,
a.created_at as created_at_U,
a.contributors_enabled as contributors_enabled_U,
a.time_zone as time_zone_U,
a.protected as protected_U,
a.translator_type as translator_type_U,
a.following as following_U,
a.listed_count as listed_count_U,
a.profile_banner_url as profile_banner_url_U,
a.id as id_U,
b.*,
d."Country_league",d."League ",d."country",d."name" as nom,d."club",
c."t_id",cc.last_tw
FROM 
  public."BASE_TWEETOS" as a 
	LEFT JOIN   public."BASE_TWEETS" as b ON a.screen_name = b.id_twit
	LEFT JOIN   public."ref_liaison" as c ON a.screen_name = c.screen_name

	LEFT JOIN   public."footballers" as d ON c."t_id" = d."t_id"

	LEFT JOIN   public."TWEET_MIN" as cc ON a.screen_name = cc.screen_name
;


DELETE FROM "Mix2"  USING "Mix2"  alias 
  WHERE "Mix2".id = alias.id AND 
    "Mix2".retweet_count < alias.retweet_count;

delete from public."Mix2" 
    where exists (select 1
                  from "Mix2" t2
                  where t2.id = "Mix2".id and

                        t2.ctid > "Mix2".ctid
                 );


				 
				 