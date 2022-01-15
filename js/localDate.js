/**
 * 数字を2桁の文字列に変換する
 * @param {*} _value 二桁表記する数値
 * @returns 
 */
function formatTo2DigitText(_value) {
    // 2桁以上はそのまま処理せず返す
    if (_value > 99) return _value.toString();

    return _value <= 9 ? "0" + _value.toString() : _value.toString();
}

/**
 * 数字を3桁の文字列に変換する
 * @param {*} _value 二桁表記する数値
 * @returns 
 */
function formatTo3DigitText(_value) {
    // 3桁以上はそのまま処理せず返す
    if (_value > 999) return _value.toString();

    if (_value <= 9) return "00" + _value.toString();
    else if (_value <= 99) return "0" + _value.toString();
    else return _value.toString();
}

/**
 * 指定の時差が反映されたDateインスタンスを取得する
 * @param {*} _timeDiffInHour 時差の値（UTC基準）
 * @returns 
 */
function getLocalDate(_timeDiffInHour) {
    var date = new Date();

    let utcYear = date.getUTCFullYear();
    let utcMonth = date.getUTCMonth();
    let utcDay = date.getUTCDate();
    let utcHour = date.getUTCHours();

    var localYear = utcYear;
    var localMonth = utcMonth;
    var localDay = utcDay;
    var localHour = utcHour + _timeDiffInHour;

    // Add date
    if (utcHour + _timeDiffInHour >= 24) {
        localHour = (utcHour + _timeDiffInHour) % 24;
        localDay += 1;

        // Day validation
        var monthType = 0; // 0 = Feb, 1 = Apr/Jun/Sept/Nov, 2 = Jan/Mar/May/July/Aug/Oct, 3 = Dec
        if (utcMonth == 2 + 1) monthType = 0;
        else if (utcMonth == 4 + 1 || utcMonth == 6 + 1 || utcMonth == 9 + 1 || utcMonth == 11 + 1) monthType = 1;
        else monthType = 2;

        switch (monthType) {
            case 0: // Feb
                if (localYear % 4 == 0) {
                    if (localDay > 29) {
                        localDay = 1;
                        localMonth += 1;
                    }
                }
                else if (localDay > 28) {
                    localDay = 1;
                    localMonth += 1;
                }
                break;
            case 1: // Apr/Jun/Sept/Nov
                if (localDay > 30) {
                    localDay = 1;
                    localMonth += 1;
                }
                break;
            case 2: // Jan/Mar/May/July/Aug/Oct/Dec
                if (localDay > 31) {
                    localDay = 1;
                    localMonth += 1;
                }
                break;
            case 3: // Dec (To Next Year)
                if (localDay > 31) {
                    localDay = 1;
                    localMonth = 1;
                    localYear += 1;
                }
                break;
        }
    }
    // Subtract Date
    else if (utcHour + _timeDiffInHour < 0) {
        localHour = 24 + (utcHour + _timeDiffInHour);
        localDay -= 1;

        // Day validation
        if (localDay <= 0) {

            var prevMonthType = 0; // 0 = Feb, 1 = Apr/Jun/Sept/Nov, 2 = Jan/Mar/May/July/Aug/Oct, 3 = Dec(PrevYear)
            if (utcMonth == 3 + 1) prevMonthType = 0;
            else if (utcMonth == 5 + 1 || utcMonth == 7 + 1 || utcMonth == 10 + 1 || utcMonth == 12 + 1) prevMonthType = 1;
            else if (utcMonth == 1 + 1) 3;
            else prevMonthType = 2;

            switch (prevMonthType) {
                case 0: // Feb
                    if (localYear % 4 == 0) {
                        localDay = 29;
                        localMonth -= 1;
                    }
                    else {
                        localDay = 28;
                        localMonth -= 1;
                    }
                    break;
                case 1: // Apr/Jun/Sept/Nov
                    localDay = 30;
                    localMonth -= 1;
                    break;
                case 2: // Jan/Mar/May/July/Aug/Oct
                    localDay = 31;
                    localMonth -= 1;
                    break;
                case 3: // Dec (To Prev Year)
                    localDay = 31;
                    localMonth = 12;
                    localYear -= 1;
                    break;
            }
        }
    }

    // Apply date updates
    date.setFullYear(localYear);
    date.setMonth(localMonth);
    date.setDate(localDay);
    date.setHours(localHour);

    return date;
}

/**
 * 曜日の情報を日本語一文字で取得する
 * @param {*} _dayOfWeek 
 * @returns 
 */
function getWeekdayInShortJa(_dayOfWeek) {
    switch (_dayOfWeek) {
        case 1:
            return "月";
        case 2:
            return "火";
        case 3:
            return "水";
        case 4:
            return "木";
        case 5:
            return "金";
        case 6:
            return "土";
        case 7:
            return "日";
        default:
            return "";
    }
}

/**
 * 曜日の情報を英語短縮表記で取得する
 * @param {*} _dayOfWeek 
 * @returns 
 */
function getWeekdayInShortEn(_dayOfWeek) {
    switch (_dayOfWeek) {
        case 1:
            return "Mon";
        case 2:
            return "Tue";
        case 3:
            return "Wed";
        case 4:
            return "Thu";
        case 5:
            return "Fri";
        case 6:
            return "Sat";
        case 7:
            return "Sun";
        default:
            return "";
    }

}

