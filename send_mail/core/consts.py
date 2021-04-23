from enum import Enum

RET_CODE_SUCCESS_1ST_CHAR = "0"
CUSTOMER_ID_KEY_IN_IR_CONFIG_PARAM = "fx_forex_seqnum"
CUSTOMER_ID_DEMO_KEY_IN_IR_CONFIG_PARAM = "demo_seq_number"
ACCOUNT_LEVERAGE = "fx_indv_max_leverage"
FX_DEMO_GROUP = "fx_demo_group"
FX_WHITELABEL_CODE = "fx_whitelabel_code"
CUSTOMER_ID_NUM_FORMAT = "06"
EMAIL_FAILED_MESSAGE = (
    "There are some problems so we cannot send you confirm email. "
    "Please contact us for more support"
)
DEMO_ACCOUNT_MT5_INITIAL = 10000000
KEY_SERVER_NAME_REGIS_DEMO = "fx_webapi_url"
TOKEN_LENGTH = 32


class IrAttachmentMimeType(Enum):
    IMAGE_PNG = "image/png"


class IrAttachmentType(Enum):
    BINARY = "binary"


class IrAttachmentResModel(Enum):
    RES_PARTNER = "res.partner"


class IrAttachmentResModelName(Enum):
    CONTACT = "Contact"


class IrAttachmentName(Enum):
    IMAGE = "image"
    IMAGE_MEDIUM = "image_medium"
    IMAGE_SMALL = "image_small"


class IrAttachmentImageFileSize(Enum):
    CORP_IMAGE = 22053
    CORP_IMAGE_MEDIUM = 16005
    CORP_IMAGE_SMALL = 5310
    INDI_IMAGE = 16880
    INDI_IMAGE_MEDIUM = 12197
    INDI_IMAGE_SMALL = 4007


class IrAttachmentImageStoreFname(Enum):
    CORP_IMAGE = "bc/bcf4681543800e92a17d594681f0a8454721abe3"
    CORP_IMAGE_MEDIUM = "74/74a14bf0ee0bcd996563d1c14b399b4ae76e70b3"
    CORP_IMAGE_SMALL = "8a/8aab592abe20a53515ccdd69db7bfb3a20f91ace"
    INDI_IMAGE = "78/78e4997aacd6b6bed81ad17ddf7e8d927c8b562b"
    INDI_IMAGE_MEDIUM = "f7/f7e9a685e63ba4727d860e07cdbe7afca6d0c533"
    INDI_IMAGE_SMALL = "83/836b0e49d838dcbe3c20616a04a1e2f431a4cdb8"


class IrAttachmentImageCheckSum(Enum):
    CORP_IMAGE = "bcf4681543800e92a17d594681f0a8454721abe3"
    CORP_IMAGE_MEDIUM = "74a14bf0ee0bcd996563d1c14b399b4ae76e70b3"
    CORP_IMAGE_SMALL = "8aab592abe20a53515ccdd69db7bfb3a20f91ace"
    INDI_IMAGE = "78e4997aacd6b6bed81ad17ddf7e8d927c8b562b"
    INDI_IMAGE_MEDIUM = "f7e9a685e63ba4727d860e07cdbe7afca6d0c533"
    INDI_IMAGE_SMALL = "836b0e49d838dcbe3c20616a04a1e2f431a4cdb8"


class TokenPrefix(Enum):
    ACCESS = "ACCESS_"
    PWD_CHANGE = "CH_PWD_"
    EMAIL_CHANGE = "CH_EMAIL_"


class EastAsianWidth(Enum):
    Ambiguous = "A"
    Fullwidth = "F"
    Halfwidth = "H"
    Neutral = "N"
    Narrow = "Na"
    Wide = "W"


class ResPartnerColor(Enum):
    COLOR_INDI = 4
    COLOR_CORP = 9


class IrConfigParameterKey(Enum):
    fx_funding_min_deposit = "fx_funding_min_deposit"
    fx_funding_min_withdraw = "fx_funding_min_withdraw"
    fx_funding_max_deposit = "fx_funding_max_deposit"
    fx_funding_max_withdraw = "fx_funding_max_withdraw"


class ResPartnerLang(Enum):
    EN_US = "en_US"
    JA_JP = "ja_JP"


class ContentType(Enum):
    PDF = "application/pdf"
    CSV = "text/csv"


class FileType(Enum):
    PDF = "pdf"
    CSV = "csv"


class ResPartnerType(Enum):
    PIC = "contact_pic"
    SUB_RULER = "contact_subruler"


class FxResPartnerStage(Enum):
    ApplicationNew = 1
    DocumentWaiting = 2
    AuditCompleted = 3
    OpenCompleted = 4
    ClosedAccount = 5
    DocumentLack = 6
    ApplicationCancel = 7
    Reject = 8
    LockAccount = 9


class FxResPartnerStageCode(Enum):
    ApplicationNew = "an"
    DocumentWaiting = "dw"
    AuditCompleted = "ad"
    OpenCompleted = "oc"
    ClosedAccount = "ca"
    DocumentLack = "dl"
    ApplicationCancel = "ac"
    Reject = "rj"
    LockAccount = "la"


STAGE_FOR_CHECK_EMAIL_EXIST = [
    FxResPartnerStage.ApplicationNew.value,
    FxResPartnerStage.DocumentWaiting.value,
    FxResPartnerStage.AuditCompleted.value,
    FxResPartnerStage.OpenCompleted.value,
    FxResPartnerStage.DocumentLack.value,
    FxResPartnerStage.LockAccount.value,
]

STAGE_FOR_CHECK_EMAIL_FORGOT_PWD = [FxResPartnerStage.OpenCompleted.value]
STAGE_FOR_GET_USER_LOGIN = [FxResPartnerStage.OpenCompleted.value]


class UserType(Enum):
    INDIVIDUAL = "individual"
    CORPORATION = "corporation"


class UserEditProcess(Enum):
    APPROVED = "A"
    INPROGRESS = "P"


class NewsScope(Enum):
    ALL = "A"
    PRIVATE = "P"
    GROUP = "G"


class NewsAgreement(Enum):
    NEWS_NOT_AGREEMENT = 0
    NEWS_AGREEMENT = 1


class DeviceType(Enum):
    MOBILE = "Mobile"
    FRONT_WEB = "FrontWeb"


class FxNewsType(Enum):
    IMPORTANT = "0"
    SYSTEM = "1"
    CAMPAIGN = "2"
    IMPORTANT_SYSTEM = "01"


class FxFundingMethod(Enum):
    QUICK_DEPOSIT = "qd"
    BANK_TRANSFER = "bt"
    INTERNAL_TRANSFER = "it"


class FxFundingType(Enum):
    DEPOSIT = "d"
    WITHDRAW = "w"
    ALL = "0"


class FxFundingStatus(Enum):
    COMPLETED = "1"
    CANCEL = "2"
    IN_PROGRESS = "3"  # -> IN_PROGRESS create deposit(default state)
    NEW = "4"  # -> NEW create withdraw(default state)


class ReportContentType(Enum):
    PDF = "application/pdf"
    CSV = "text/csv"


class FxNewsNewsScope(Enum):
    ALL = "A"
    PRIVATE = "P"


class BillingStatus(Enum):
    SUCCESS = "00"
    IN_PROGRESS = "09"


class MT5Trading(Enum):
    BALANCE = 2


class BJPResCode(Enum):
    OK = "00"
    PROCESSING = "09"
    TIMEOUT = "15"
    MAINTAIN = "16"
    BANK_ERROR = "19"
    INFO_ERROR = "21"
    SHOP_ERROR = "29"
    CANCEL = "32"
    USER_ERROR = "39"
    SUBMIT_ERROR = "83"
    UNKNOWN = "91"
    UNPAID = "92"
    MISMATCH = "93"
    PAYMENT = "99"


class StateEmail(Enum):
    SENT = "sent"
    EXCEPTION = "exception"


class RegAccountType(Enum):
    # use for save account type in fx_res_partner
    FX = "01"
    CFD_INDEX = "02"
    CFD_COMMODITY = "03"


class AccountType(Enum):
    # use for save account type in fx_res_partner_trading
    FX = "1"
    CFD_INDEX = "2"
    CFD_COMMUNITY = "3"


class AccountTypeJP(Enum):
    # use for display in mail regist demo
    FX = "FX口座ID:"
    CFD_INDEX = "株価指数CFD口座ID:"
    CFD_COMMUNITY = "商品CFD口座ID:"


class AccountTypeName(Enum):
    FX = "[FX]"
    CFD_INDEX = "[I-CFD]"
    CFD_COMMODITY = "[C-CFD]"


class FxResPartnerTradingStatus(Enum):
    CAN_NOT_TRADING = 0  # NEW OR CLOSE ORDER
    NORMAL = 1  # ALREADY CREATED MT5 ACC
    ONLY_CLOSE_POSITIONS = 2
    NEW = 3  # WAITING FOR CREATE MT5 ACC
    CLOSED = 4
    CANCEL = 7


class MT5Group(Enum):
    FX_COMP = r"10\PhillipMT5_Corp"
    FX_INDI = r"10\PhillipMT5_Indi"
    B2B_F1 = r"10\PhillipMT5_B2B_F1"
    B2B_C1 = r"10\PhillipMT5_B2B_C1"
    B2B_C2 = r"10\PhillipMT5_B2B_C2"
    I_CFD_INDI = r"10\PhillipMT5_Index_Indi"
    I_CFD_COMP = r"10\PhillipMT5_Index_Corp"
    C_CFD_COMP = r"10\PhillipMT5_Com_Corp"
    C_CFD_INDI = r"10\PhillipMT5_Com_Indi"
    I_CFD_INDI_F1 = r"10\PhillipMT5_Index_B2B_F1"
    I_CFD_INDI_C1 = r"10\PhillipMT5_Index_B2B_C1"
    C_CFD_COMP_F1 = r"10\Phillip_Com_B2B_F1"
    C_CFD_COMP_C1 = r"10\Phillip_Com_B2B_C1"


class MT5LandingPageCode(Enum):
    B2B_F1 = "pl_b2bf1"
    B2B_C1 = "pl_b2bc1"


class BizGroupType(Enum):
    INTERNAL = "it"
    B2B = "bb"


B2B_LP_CODES = [MT5LandingPageCode.B2B_F1.value, MT5LandingPageCode.B2B_C1.value]


FX_GROUP = [MT5Group.FX_COMP.value, MT5Group.FX_INDI.value]

I_CFD_GROUP = [MT5Group.I_CFD_COMP.value, MT5Group.I_CFD_INDI.value]
C_CFD_GROUP = [MT5Group.C_CFD_COMP.value, MT5Group.C_CFD_INDI.value]
B2B_GROUP_FX = [MT5Group.B2B_C1.value, MT5Group.B2B_F1.value, MT5Group.B2B_C2.value]
I_CFD_B2B_GROUP = [MT5Group.I_CFD_INDI_F1.value, MT5Group.I_CFD_INDI_C1.value]
C_CFD_B2B_GROUP = [MT5Group.C_CFD_COMP_F1.value, MT5Group.C_CFD_COMP_C1.value]

# State for use can login if user use trading account id in fx_res_partner_trading
AVAILABLE_STATE_ACCOUNT = [
    FxResPartnerTradingStatus.NORMAL.value,
    FxResPartnerTradingStatus.CAN_NOT_TRADING.value,
    FxResPartnerTradingStatus.ONLY_CLOSE_POSITIONS.value,
]

# state check user can not create new account in fx_res_partner_trading
STATE_CAN_NOT_CREATE_ACCOUNT = [
    FxResPartnerTradingStatus.NORMAL.value,
    FxResPartnerTradingStatus.CAN_NOT_TRADING.value,
    FxResPartnerTradingStatus.ONLY_CLOSE_POSITIONS.value,
    FxResPartnerTradingStatus.NEW.value,
    FxResPartnerTradingStatus.CLOSED.value,
]


class MT5GroupName(Enum):
    FX = "FX"
    CFD_INDEX = "I-CFD"
    CFD_COMMODITY = "C-CFD"
    ALL_GROUP = "all"
    B2B_GROUP = "B2B"


class NewsGroup(Enum):
    All = "IT_A"
    FX = "IT_FX"
    I_CFD = "IT_CFDI"
    C_CFD = "IT_CFDC"
    B2B_ALL = "B2B_A"
    B2B_FX = "B2B_FX"
    B2B_I_CFD = "B2B_CFDI"
    B2B_C_CFD = "B2B_CFDC"


GENDER_MALE = "M"
GENDER_FEMALE = "F"
GENDER_SHOW = {GENDER_MALE: "男性", GENDER_FEMALE: "女性"}

BANK_TRANSFER_ERROR_CODE = {
    "00": "Payment Completed (OK)",
    "09": "Processing",
    "15": "Outside of Handling Time",
    "16": "Service Maintenance",
    "19": "Error Caused by Bank",
    "21": "Input Information Error",
    "29": "Error Caused by Shop",
    "32": "User Cancel",
    "39": "Error Caused by User",
    "83": "Double Submission Error",
    "91": "Other Error (unknown)",
    "92": "Other Error (unpaid)",
    "93": "Holder Name Mismatch",
    "99": "Payment Error",
}

# Special bank code mapping for Mizuho, UFJ
BANK_CODE_MAP = {"0003": "0001", "0008": "0005"}

FIN_PURPOSE_INDIVIDUAL = [
    "indi_income",
    "indi_capital",
    "indi_investable",
    "indi_invest_verification",
    "indi_inv_purpose",
    "indi_other_purpose",
    "indi_source",
    "indi_other_source",
    "indi_fx_exp",
    "indi_cfd_exp",
    "indi_stock_exp",
    "indi_margin_exp",
    "indi_comm_exp",
    "indi_other_exp_yn",
    "indi_other_fin_name",
    "indi_other_fin_exp",
]

FIN_PURPOSE_CORPORATION = [
    "corp_annual_sales",
    "corp_sales_after_tax",
    "corp_capital",
    "corp_investable",
    "corp_inv_purpose",
    "corp_other_inv",
    "corp_source",
    "corp_other_source",
    "corp_pic_fx_exp",
    "corp_pic_cfd_exp",
    "corp_pic_stock_exp",
    "corp_pic_margin_exp",
    "corp_pic_comm_exp",
    "corp_pic_other_exp_yn",
    "corp_pic_other_name_exp",
    "corp_pic_other_exp",
]

STATE_EN = ["", "Completed", "Cancel", "In-progress", "New"]
STATE_JP = ["", "完了", "キャンセル", "処理中", ""]

RINGI_NAME_WAIT_PROCES = "変更依頼"
RINGI_TYPE_PROCESS = "process"
RINGI_TYPE_ADD_ACCOUNT = "add_account"
RINGI_NAME_ADD_ACCOUNT = "口座の追加依頼"
RINGI_DESC_ADD_ACCOUNT = "<p>口座の追加</p>"

RINGI_STATE_NEW = "new"
RINGI_STATE_DOC_WAIT = "document_waiting"
RINGI_STATE_REJECT = "reject"
RINGI_STATE_RECOGNIZE = "recognize"

RINGI_PRI_LOW = "low"
RINGI_PRI_NORMAL = "normal"
RINGI_PRI_HIGH = "high"

# Default create_uid / write_uid
DEFAULT_API_UID = 1

# Phillip Company ID
DEFAULT_PHILLIP_WL = 1

# Admin UID, assign when create ringi
SYSTEM_UID = 1
ADMIN_UID = 2

# Define email template name
EMAIL_TEMPLATE_PASS_RESET = "phillip_password_reset"
EMAIL_TEMPLATE_WITHDRAW_REQUEST = "phillip_withdraw_request"
EMAIL_TEMPLATE_WITHDRAW_FAIL = "phillip_withdraw_failed"
EMAIL_TEMPLATE_NEW_REGIST = "phillip_registration_new"
EMAIL_TEMPLATE_DEMO_REGIST = "phillip_registration_demo"
EMAIL_TEMPLATE_PASS_CHANGED = "phillip_password_changed"
EMAIL_TEMPLATE_MAIL_RESET = "phillip_email_reset"
EMAIL_TEMPLATE_MAIL_CHANGED = "phillip_email_changed"
EMAIL_TEMPLATE_MAIL_LOCK_ACCOUNT = "phillip_account_locked"
EMAIL_TEMPLATE_ADD_MORE_REGIST = "phillip_registration_addmore"
EMAIL_TEMPLATE_BANK_CHANGED = "phillip_bank_change"


# Phillip White Lable Code
WL_PHILLIP = "10"
WL_HASHDASH = "20"

# Payment Gateway Code
# BJP => Payment Gateway BJP
# BTF => Bank Transfer
PW_BJP = "BJP"
PW_BTF = "BTF"

# Funding fee type
FEE_AMOUNT = "a"
FEE_PERCENT = "p"

# Demo account type
DEMO_ACCOUNT_TYPE = "99"

# Device type
DEVICE_TYPE = {
    "pc": "PC Web",
    "android": "Android",
    "iphone": "Iphone",
    "ipad": "Ipad",
    "none": "undefined",
}

# For cached config
# Cache model data, default: 15 min
CACHED_MODEL_TIMEOUT = 15 * 60
CACHED_KEY_LOGIN_FAILED = "fx:num_login_failed:{user_id}"
CACHED_KEY_DEVICE_USER = "fx:device_user:{user_id}"

# Margin call mode
MC_MODE_MARGINCALL = "mc"
MC_MODE_LOSSCUT = "lc"
MC_MODE_ALL = "all"

# Type password policy
TYPE_PW_DIGIST = "digits"
TYPE_PW_LOW_CASE = "lower-case letter"
TYPE_PW_UPPER_CASE = "upper-case letter"
TYPE_PW_SYMBOLS = "symbols"

# Type password policy Japanese
JP_TYPE_PW_DIGIST = "数学"
JP_TYPE_PW_LOW_CASE = "小文字"
JP_TYPE_PW_UPPER_CASE = "大文字"
JP_TYPE_PW_SYMBOLS = "銘柄"

# right on MT5
MT5_USER_RIGHT_ENABLED = 0x0000000000000001

# Module type
MODULE_FRONT_WEB = "front_web"


# MT5 status check balance
MT5_CONNECT_ERROR = 1
MT5_NOT_ENOUGH_AMOUNT = 2
MT5_AVAILABLE_WITHDRAW = 3

# fx_news new_group values
NEWS_GROUP_ALL = "all"


# fx_funding account type search
ACCOUNT_ALL = "all"

# MT5 Length Password
MT5_PWD_MIN_LENGTH = 8
MT5_PWD_MAX_LENGTH = 30


# MT5 retcode
class MT5_RETCODE(Enum):
    NOT_ENOUGH_MONEY = "10019"


MAX_QUOREA_KEY_SIZE = 16
