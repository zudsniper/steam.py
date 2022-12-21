# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: service_quest.proto
# plugin: python-betterproto
# Last updated 21/12/2022

from dataclasses import dataclass

import betterproto

from .msg import UnifiedMessage


class ActivateProfileModifierItemRequest(UnifiedMessage, um_name="Quest.ActivateProfileModifierItem"):
    appid: int = betterproto.uint32_field(1)
    communityitemid: int = betterproto.uint64_field(2)
    activate: bool = betterproto.bool_field(3)


class ActivateProfileModifierItemResponse(UnifiedMessage, um_name="Quest.ActivateProfileModifierItem"):
    pass


@dataclass(eq=False, repr=False)
class CommunityItem(betterproto.Message):
    communityitemid: int = betterproto.uint64_field(1)
    item_type: int = betterproto.uint32_field(2)
    appid: int = betterproto.uint32_field(3)
    owner: int = betterproto.uint32_field(4)
    attributes: "list[CommunityItemAttribute]" = betterproto.message_field(5)
    used: bool = betterproto.bool_field(6)
    owner_origin: int = betterproto.uint32_field(7)
    amount: int = betterproto.int64_field(8)


@dataclass(eq=False, repr=False)
class CommunityItemAttribute(betterproto.Message):
    attributeid: int = betterproto.uint32_field(1)
    value: int = betterproto.uint64_field(2)


class GetCommunityInventoryRequest(UnifiedMessage, um_name="Quest.GetCommunityInventory"):
    filter_appids: list[int] = betterproto.uint32_field(1)


class GetCommunityInventoryResponse(UnifiedMessage, um_name="Quest.GetCommunityInventory"):
    items: "list[CommunityItem]" = betterproto.message_field(1)


class GetCommunityItemDefinitionsRequest(UnifiedMessage, um_name="Quest.GetCommunityItemDefinitions"):
    appid: int = betterproto.uint32_field(1)
    item_type: int = betterproto.uint32_field(3)
    language: str = betterproto.string_field(4)
    broadcast_channel_id: int = betterproto.uint64_field(5)
    keyvalues_as_json: bool = betterproto.bool_field(6)


class GetCommunityItemDefinitionsResponse(UnifiedMessage, um_name="Quest.GetCommunityItemDefinitions"):
    item_definitions: "list[GetCommunityItemDefinitionsResponseItemDefinition]" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class GetCommunityItemDefinitionsResponseItemDefinition(betterproto.Message):
    item_type: int = betterproto.uint32_field(1)
    appid: int = betterproto.uint32_field(2)
    item_name: str = betterproto.string_field(3)
    item_title: str = betterproto.string_field(4)
    item_description: str = betterproto.string_field(5)
    item_image_small: str = betterproto.string_field(6)
    item_image_large: str = betterproto.string_field(7)
    item_key_values: str = betterproto.string_field(8)
    item_series: int = betterproto.uint32_field(9)
    item_class: int = betterproto.uint32_field(10)
    editor_accountid: int = betterproto.uint32_field(11)
    active: bool = betterproto.bool_field(12)
    item_image_composed: str = betterproto.string_field(13)
    item_image_composed_foil: str = betterproto.string_field(14)
    deleted: bool = betterproto.bool_field(15)
    item_last_changed: int = betterproto.uint32_field(16)
    broadcast_channel_id: int = betterproto.uint64_field(17)
    item_movie_webm: str = betterproto.string_field(18)
    item_movie_mp4: str = betterproto.string_field(19)
    item_movie_webm_small: str = betterproto.string_field(20)
    item_movie_mp4_small: str = betterproto.string_field(21)


class GetNumTradingCardsEarnedRequest(UnifiedMessage, um_name="Quest.GetNumTradingCardsEarned"):
    timestamp_start: int = betterproto.uint32_field(1)
    timestamp_end: int = betterproto.uint32_field(2)


class GetNumTradingCardsEarnedResponse(UnifiedMessage, um_name="Quest.GetNumTradingCardsEarned"):
    num_trading_cards: int = betterproto.uint32_field(1)


class SetVirtualItemRewardDefinitionRequest(UnifiedMessage, um_name="Quest.SetVirtualItemRewardDefinition"):
    eventid: int = betterproto.int32_field(1)
    itemsdefs: "list[CVirtualItemRewardDefinition]" = betterproto.message_field(2)
    action: int = betterproto.int32_field(3)


class SetVirtualItemRewardDefinitionResponse(UnifiedMessage, um_name="Quest.SetVirtualItemRewardDefinition"):
    pass


class VirtualItemRewardDefinitionRequest(UnifiedMessage, um_name="Quest.VirtualItemRewardDefinition"):
    eventid: int = betterproto.int32_field(1)
    include_inactive: bool = betterproto.bool_field(2)


class VirtualItemRewardDefinitionResponse(UnifiedMessage, um_name="Quest.VirtualItemRewardDefinition"):
    rewards: "list[CVirtualItemRewardDefinition]" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class CVirtualItemRewardDefinition(betterproto.Message):
    eventid: int = betterproto.int32_field(1)
    item_bucket: int = betterproto.uint32_field(2)
    appid: int = betterproto.uint32_field(3)
    active: bool = betterproto.bool_field(4)
    rarity: int = betterproto.uint32_field(5)
    package_to_grant: int = betterproto.uint32_field(6)
    game_item_id: int = betterproto.fixed64_field(7)
    community_item_class: int = betterproto.int32_field(8)
    community_item_type: int = betterproto.uint32_field(9)
    loyalty_point_type: int = betterproto.uint32_field(10)
    amount: int = betterproto.int64_field(11)
    rtime_time_active: int = betterproto.uint32_field(12)
    loyalty_reward_defid: int = betterproto.uint32_field(13)
    user_badge_to_grant: int = betterproto.uint32_field(14)
    user_badge_level: int = betterproto.uint32_field(15)
    virtual_item_def_id: int = betterproto.uint32_field(16)
