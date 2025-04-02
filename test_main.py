import requests
import main


def test_get_list_of_users():
    url = "https://genshin.jmp.blue/"
    response = requests.get(url)
    assert response.status_code == 20


def test_get_characters(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = [
        "albedo",
        "alhaitham",
        "aloy",
        "amber",
        "arataki-itto",
        "arlecchino",
        "ayaka",
        "ayato",
        "baizhu",
        "barbara",
        "beidou",
        "bennett",
        "candace",
        "charlotte",
        "chevreuse",
        "chiori",
        "chongyun",
        "clorinde",
        "collei",
        "cyno",
        "dehya",
        "diluc",
        "diona",
        "dori",
        "emilie",
        "eula",
        "faruzan",
        "fischl",
        "freminet",
        "furina",
        "gaming",
        "ganyu",
        "gorou",
        "hu-tao",
        "jean",
        "kachina",
        "kaeya",
        "kaveh",
        "kazuha",
        "keqing",
        "kinich",
        "kirara",
        "klee",
        "kokomi",
        "kuki-shinobu",
        "layla",
        "lisa",
        "lynette",
        "lyney",
        "mika",
        "mona",
        "mualani",
        "nahida",
        "navia",
        "neuvillette",
        "nilou",
        "ningguang",
        "noelle",
        "qiqi",
        "raiden",
        "razor",
        "rosaria",
        "sara",
        "sayu",
        "sethos",
        "shenhe",
        "shikanoin-heizou",
        "sigewinne",
        "sucrose",
        "tartaglia",
        "thoma",
        "tighnari",
        "traveler-anemo",
        "traveler-dendro",
        "traveler-electro",
        "traveler-geo",
        "traveler-hydro",
        "venti",
        "wanderer",
        "wriothesley",
        "xiangling",
        "xianyun",
        "xiao",
        "xingqiu",
        "xinyan",
        "yae-miko",
        "yanfei",
        "yaoyao",
        "yelan",
        "yoimiya",
        "yun-jin",
        "zhongli",
    ]
    mock_response.status_code = 200
    mocker.patch("requests.get", return_value=mock_response)

    result = main.get_character_data()
    assert result == mock_response.json.return_value
    requests.get.assert_called_once_with(
        "https://genshin.jmp.blue/characters", headers={"Accept": "application/json"}
    )
