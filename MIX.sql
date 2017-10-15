Drop table public."REF";
Drop table public."TWEET_MIN";
Create table public."TWEET_MIN" as SELECT 
id_twit as screen_name,max(col) as last_tw
from public."BASE_TWEETS"
GROUP BY screen_name;


Create table public."REF" as SELECT 
a.index as index,
a.follow_request_sent as follow_request_sent,
a.has_extended_profile as has_extended_profile,
a.profile_use_background_image as profile_use_background_image,
a.idd as idd,
a.default_profile as default_profile,
a.verified as verified,
a.profile_text_color as profile_text_color,
a.profile_image_url_https as profile_image_url_https,
a.profile_sidebar_fill_color as profile_sidebar_fill_color,
a.is_translator as is_translator,
a.geo_enabled as geo_enabled,
a.followers_count as followers_count,
a.profile_sidebar_border_color as profile_sidebar_border_color,
a.location as location,
a.default_profile_image as default_profile_image,
a.id_str as id_str,
a.is_translation_enabled as is_translation_enabled,
a.utc_offset as utc_offset,
a.statuses_count as statuses_count,
a.description as description,
a.friends_count as friends_count,
a.profile_link_color as profile_link_color,
a.profile_image_url as profile_image_url,
a.notifications as notifications,
a.profile_background_image_url_https as profile_background_image_url_https,
a.profile_background_color as profile_background_color,
a.profile_background_image_url as profile_background_image_url,
a.name as name,
a.lang as lang,
a.profile_background_tile as profile_background_tile,
a.favourites_count as favourites_count,
a.screen_name as screen_name,
a.url as url,
a.created_at as created_at,
a.contributors_enabled as contributors_enabled,
a.time_zone as time_zone,
a.protected as protected,
a.translator_type as translator_type,
a.following as following,
a.listed_count as listed_count,
a.profile_banner_url as profile_banner_url,
a.id as id,
d."Country_league",d."League",d."country",d."name",d."club",
c."T_ID",cc.last_tw
FROM 
  public."BASE_TWEETOS" as a 
	LEFT JOIN   public."ref_liaison" as c ON a.screen_name = c.screen_name

	LEFT JOIN   public."footballer" as d ON c."T_ID" = d."T_ID"

	LEFT JOIN   public."TWEET_MIN" as cc ON a.screen_name = cc.screen_name
;


