from .Utils import *


class Fundamental:
    def __init__(self, symbol, high52, low52, dividend_amount, dividend_yield, dividend_date, pe_ratio, peg_ratio, pb_ratio, pr_ratio, pcf_ratio, gross_margin_ttm, gross_margin_mrq, net_profit_margin_ttm, net_profit_margin_mrq, operating_margin_ttm, operating_margin_mrq, return_on_equity, return_on_assets, return_on_investment, quick_ratio, current_ratio, interest_coverage, total_debt_to_capital,
                 lt_debt_to_equity, total_debt_to_equity, eps_ttm, eps_change_percent_ttm, eps_change_year, eps_change, rev_change_year, rev_change_ttm, rev_change_in, shares_outstanding, market_cap_float, market_cap, book_value_per_share, short_int_to_float, short_int_day_to_cover, div_growth_rate3_year, dividend_pay_amount, dividend_pay_date, beta, vol1_day_avg, vol10_day_avg, vol3_month_avg):
        self.symbol = symbol
        self.high52 = high52
        self.low52 = low52
        self.dividend_amount = dividend_amount
        self.dividend_yield = dividend_yield
        self.dividend_date = dividend_date
        self.pe_ratio = pe_ratio
        self.peg_ratio = peg_ratio
        self.pb_ratio = pb_ratio
        self.pr_ratio = pr_ratio
        self.pcf_ratio = pcf_ratio
        self.gross_margin_ttm = gross_margin_ttm
        self.gross_margin_mrq = gross_margin_mrq
        self.net_profit_margin_ttm = net_profit_margin_ttm
        self.net_profit_margin_mrq = net_profit_margin_mrq
        self.operating_margin_ttm = operating_margin_ttm
        self.operating_margin_mrq = operating_margin_mrq
        self.return_on_equity = return_on_equity
        self.return_on_assets = return_on_assets
        self.return_on_investment = return_on_investment
        self.quick_ratio = quick_ratio
        self.current_ratio = current_ratio
        self.interest_coverage = interest_coverage
        self.total_debt_to_capital = total_debt_to_capital
        self.lt_debt_to_equity = lt_debt_to_equity
        self.total_debt_to_equity = total_debt_to_equity
        self.eps_ttm = eps_ttm
        self.eps_change_percent_ttm = eps_change_percent_ttm
        self.eps_change_year = eps_change_year
        self.eps_change = eps_change
        self.rev_change_year = rev_change_year
        self.rev_change_ttm = rev_change_ttm
        self.rev_change_in = rev_change_in
        self.shares_outstanding = shares_outstanding
        self.market_cap_float = market_cap_float
        self.market_cap = market_cap
        self.book_value_per_share = book_value_per_share
        self.short_int_to_float = short_int_to_float
        self.short_int_day_to_cover = short_int_day_to_cover
        self.div_growth_rate3_year = div_growth_rate3_year
        self.dividend_pay_amount = dividend_pay_amount
        self.dividend_pay_date = dividend_pay_date
        self.beta = beta
        self.vol1_day_avg = vol1_day_avg
        self.vol10_day_avg = vol10_day_avg
        self.vol3_month_avg = vol3_month_avg

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        symbol = from_str(obj.get("symbol"))
        high52 = from_int(obj.get("high52"))
        low52 = from_int(obj.get("low52"))
        dividend_amount = from_int(obj.get("dividendAmount"))
        dividend_yield = from_int(obj.get("dividendYield"))
        dividend_date = from_str(obj.get("dividendDate"))
        pe_ratio = from_int(obj.get("peRatio"))
        peg_ratio = from_int(obj.get("pegRatio"))
        pb_ratio = from_int(obj.get("pbRatio"))
        pr_ratio = from_int(obj.get("prRatio"))
        pcf_ratio = from_int(obj.get("pcfRatio"))
        gross_margin_ttm = from_int(obj.get("grossMarginTTM"))
        gross_margin_mrq = from_int(obj.get("grossMarginMRQ"))
        net_profit_margin_ttm = from_int(obj.get("netProfitMarginTTM"))
        net_profit_margin_mrq = from_int(obj.get("netProfitMarginMRQ"))
        operating_margin_ttm = from_int(obj.get("operatingMarginTTM"))
        operating_margin_mrq = from_int(obj.get("operatingMarginMRQ"))
        return_on_equity = from_int(obj.get("returnOnEquity"))
        return_on_assets = from_int(obj.get("returnOnAssets"))
        return_on_investment = from_int(obj.get("returnOnInvestment"))
        quick_ratio = from_int(obj.get("quickRatio"))
        current_ratio = from_int(obj.get("currentRatio"))
        interest_coverage = from_int(obj.get("interestCoverage"))
        total_debt_to_capital = from_int(obj.get("totalDebtToCapital"))
        lt_debt_to_equity = from_int(obj.get("ltDebtToEquity"))
        total_debt_to_equity = from_int(obj.get("totalDebtToEquity"))
        eps_ttm = from_int(obj.get("epsTTM"))
        eps_change_percent_ttm = from_int(obj.get("epsChangePercentTTM"))
        eps_change_year = from_int(obj.get("epsChangeYear"))
        eps_change = from_int(obj.get("epsChange"))
        rev_change_year = from_int(obj.get("revChangeYear"))
        rev_change_ttm = from_int(obj.get("revChangeTTM"))
        rev_change_in = from_int(obj.get("revChangeIn"))
        shares_outstanding = from_int(obj.get("sharesOutstanding"))
        market_cap_float = from_int(obj.get("marketCapFloat"))
        market_cap = from_int(obj.get("marketCap"))
        book_value_per_share = from_int(obj.get("bookValuePerShare"))
        short_int_to_float = from_int(obj.get("shortIntToFloat"))
        short_int_day_to_cover = from_int(obj.get("shortIntDayToCover"))
        div_growth_rate3_year = from_int(obj.get("divGrowthRate3Year"))
        dividend_pay_amount = from_int(obj.get("dividendPayAmount"))
        dividend_pay_date = from_str(obj.get("dividendPayDate"))
        beta = from_int(obj.get("beta"))
        vol1_day_avg = from_int(obj.get("vol1DayAvg"))
        vol10_day_avg = from_int(obj.get("vol10DayAvg"))
        vol3_month_avg = from_int(obj.get("vol3MonthAvg"))
        return Fundamental(symbol, high52, low52, dividend_amount, dividend_yield, dividend_date, pe_ratio, peg_ratio, pb_ratio, pr_ratio, pcf_ratio, gross_margin_ttm, gross_margin_mrq, net_profit_margin_ttm, net_profit_margin_mrq, operating_margin_ttm, operating_margin_mrq, return_on_equity, return_on_assets, return_on_investment, quick_ratio, current_ratio, interest_coverage, total_debt_to_capital,
                           lt_debt_to_equity, total_debt_to_equity, eps_ttm, eps_change_percent_ttm, eps_change_year, eps_change, rev_change_year, rev_change_ttm, rev_change_in, shares_outstanding, market_cap_float, market_cap, book_value_per_share, short_int_to_float, short_int_day_to_cover, div_growth_rate3_year, dividend_pay_amount, dividend_pay_date, beta, vol1_day_avg, vol10_day_avg, vol3_month_avg)

    def to_dict(self):
        result = {}
        result["symbol"] = from_str(self.symbol)
        result["high52"] = from_int(self.high52)
        result["low52"] = from_int(self.low52)
        result["dividendAmount"] = from_int(self.dividend_amount)
        result["dividendYield"] = from_int(self.dividend_yield)
        result["dividendDate"] = from_str(self.dividend_date)
        result["peRatio"] = from_int(self.pe_ratio)
        result["pegRatio"] = from_int(self.peg_ratio)
        result["pbRatio"] = from_int(self.pb_ratio)
        result["prRatio"] = from_int(self.pr_ratio)
        result["pcfRatio"] = from_int(self.pcf_ratio)
        result["grossMarginTTM"] = from_int(self.gross_margin_ttm)
        result["grossMarginMRQ"] = from_int(self.gross_margin_mrq)
        result["netProfitMarginTTM"] = from_int(self.net_profit_margin_ttm)
        result["netProfitMarginMRQ"] = from_int(self.net_profit_margin_mrq)
        result["operatingMarginTTM"] = from_int(self.operating_margin_ttm)
        result["operatingMarginMRQ"] = from_int(self.operating_margin_mrq)
        result["returnOnEquity"] = from_int(self.return_on_equity)
        result["returnOnAssets"] = from_int(self.return_on_assets)
        result["returnOnInvestment"] = from_int(self.return_on_investment)
        result["quickRatio"] = from_int(self.quick_ratio)
        result["currentRatio"] = from_int(self.current_ratio)
        result["interestCoverage"] = from_int(self.interest_coverage)
        result["totalDebtToCapital"] = from_int(self.total_debt_to_capital)
        result["ltDebtToEquity"] = from_int(self.lt_debt_to_equity)
        result["totalDebtToEquity"] = from_int(self.total_debt_to_equity)
        result["epsTTM"] = from_int(self.eps_ttm)
        result["epsChangePercentTTM"] = from_int(self.eps_change_percent_ttm)
        result["epsChangeYear"] = from_int(self.eps_change_year)
        result["epsChange"] = from_int(self.eps_change)
        result["revChangeYear"] = from_int(self.rev_change_year)
        result["revChangeTTM"] = from_int(self.rev_change_ttm)
        result["revChangeIn"] = from_int(self.rev_change_in)
        result["sharesOutstanding"] = from_int(self.shares_outstanding)
        result["marketCapFloat"] = from_int(self.market_cap_float)
        result["marketCap"] = from_int(self.market_cap)
        result["bookValuePerShare"] = from_int(self.book_value_per_share)
        result["shortIntToFloat"] = from_int(self.short_int_to_float)
        result["shortIntDayToCover"] = from_int(self.short_int_day_to_cover)
        result["divGrowthRate3Year"] = from_int(self.div_growth_rate3_year)
        result["dividendPayAmount"] = from_int(self.dividend_pay_amount)
        result["dividendPayDate"] = from_str(self.dividend_pay_date)
        result["beta"] = from_int(self.beta)
        result["vol1DayAvg"] = from_int(self.vol1_day_avg)
        result["vol10DayAvg"] = from_int(self.vol10_day_avg)
        result["vol3MonthAvg"] = from_int(self.vol3_month_avg)
        return result


class Instrument:
    def __init__(self, cusip, symbol, description, exchange, asset_type, fundamental):
        self.cusip = cusip
        self.symbol = symbol
        self.description = description
        self.exchange = exchange
        self.asset_type = asset_type
        self.fundamental = fundamental

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        cusip = from_str(obj.get("cusip"))
        symbol = from_str(obj.get("symbol"))
        description = from_str(obj.get("description"))
        exchange = from_str(obj.get("exchange"))
        asset_type = from_str(obj.get("assetType"))
        fundamental = Fundamental.from_dict(obj.get("fundamental"))
        return Instrument(cusip, symbol, description, exchange, asset_type, fundamental)

    def to_dict(self):
        result = {}
        result["cusip"] = from_str(self.cusip)
        result["symbol"] = from_str(self.symbol)
        result["description"] = from_str(self.description)
        result["exchange"] = from_str(self.exchange)
        result["assetType"] = from_str(self.asset_type)
        result["fundamental"] = to_class(Fundamental, self.fundamental)
        return result


def instrument_from_dict(s):
    return Instrument.from_dict(s)


def instrument_to_dict(x):
    return to_class(Instrument, x)
