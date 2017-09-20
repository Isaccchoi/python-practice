"""
class NaverWebtoonCrawler생성
    초기화메서드
        webtoon_id
        episode_list (빈 list)
            를 할당

    인스턴스 메서드
        def get_episode_list(self, page)
            해당 페이지의 episode_list를 생성, self.episode_list에 할당

        def clear_episode_list(self)
            자신의 episode_list를 빈 리스트로 만듬

        def get_all_episode_list(self)
            webtoon_id의 모든 episode를 생성

        def add_new_episode_list(self)
            새로 업데이트된 episode목록만 생성

"""
import pickle
import utils


class NaverWebtoonCrawler:
    def __init__(self, webtoon_id):
        self.webtoon_id = webtoon_id
        self.episode_list = list()

    @property
    def total_episode_count(self):
        """
        webtoon_id에 해당하는 실제 웹툰의 총 episode수를 리턴
        requests를 사용
        :return: 총 episode수 (int)
        """
        el = utils.get_webtoon_episode_list(self.webtoon_id)
        return int(el[0].no)

    @property
    def up_to_date(self):
        """
        현재 가지고있는 episode_list가 웹상의 최신 episode까지 가지고 있는지
        :return: boolean값
        """
        last_episode_web = self.total_episode_count
        last_episode_local = utils.get_last_episode_local(self.webtoon_id)
        if last_episode_web == last_episode_local:
            return True
        else:
            return False

    def update_episode_list(self, force_update=False):
        """
        self.episode_list에 존재하지 않는 episode들을 self.episode_list에 추가
        :param force_update: 이미 존재하는 episode도 강제로 업데이트
        :return: 추가된 episode의 수 (int)
        """
        # force_update 가 True일 경우 웹상의 최신 번호를 가져와 1번까지 돈다.
        if force_update:
            result = self.total_episode_count
            count = result
            page = (count // 10) + 1
            while page > 0 & count > 0:
                new_episode_list = utils.get_webtoon_episode_list(self.webtoon_id, page)
                if count < 10:
                    for epi in new_episode_list[:count]:
                        episode_info_string = f"{epi.no}|{epi.image_url}|{epi.title}|{epi.rate}|{epi.date}"
                        self.episode_list.insert(0, episode_info_string)
                    page = 0
                    count = 0
                else:
                    # range에 마지막 끝나는 숫자는 실제 원하는 숫자 +1을 해줘야 하므로 page에 1을 더해준다
                    for i in range(1, page + 1):
                        for epi in new_episode_list:
                            episode_info_string = f"{epi.no}|{epi.image_url}|{epi.title}|{epi.rate}|{epi.date}"
                            self.episode_list.insert(0, episode_info_string)
                    count -= 10
                    page -= 1
            return result

        if self.up_to_date:
            return 0
        else:
            # last_episode_web은 웹상의 최신화의 번호(int)를 넣어준다
            last_episode_web = self.total_episode_count
            # last_episode_local은 로컬에 저장되어 있는 번호중 최신 번호(int)를 넣어준다.
            last_episode_local = utils.get_last_episode_local(self.webtoon_id)
            result = last_episode_web - last_episode_local
            count = result
        # 한 페이지에 10개의 화가 들어가므로 10화당 1페이지를 추가해준다.
        # 리스트와 달리 홈페이지에서는 첫페이지가 1이므로 +1을 추가해준다.
        page = (count // 10) + 1
        while page > 0 & count > 0:
            new_episode_list = utils.get_webtoon_episode_list(self.webtoon_id, page)
            if count < 10:
                for epi in new_episode_list[:count]:
                    episode_info_string = f"{epi.no}|{epi.image_url}|{epi.title}|{epi.rate}|{epi.date}"
                    self.episode_list.insert(0, episode_info_string)
                page = 0
                count = 0
            else:
                # range에 마지막 끝나는 숫자는 실제 원하는 숫자 +1을 해줘야 하므로 page에 1을 더해준다
                for i in range(1, page + 1):
                    for epi in new_episode_list:
                        episode_info_string = f"{epi.no}|{epi.image_url}|{epi.title}|{epi.rate}|{epi.date}"
                        self.episode_list.insert(0, episode_info_string)
                count -= 10
                page -= 1
        return result

    def load(self, path=None):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일의 내용을 불러와
        pickle로 self.episode_list를 복원
        :return:
        """
        if not path:
            try:
                self.episode_list = pickle.load(f"db/{self.webtoon_id}.txt")
            except:
                return False
            return True
        else:
            try:
                self.episode_list = pickle.load(f"{path}")
            except:
                return False
            return True

    def save(self, path=None):
        """
        현재폴더를 기준으로 db/<webtoon_id>.txt 파일에
        pickle로 self.episode_list를 저장
        :return: 성공여부
        """
        if not path:
            try:
                pickle.dump(self.episode_list, open(f"db/{self.webtoon_id}.txt"), 'wb')
            except:
                return False
            return True
        else:
            try:
                pickle.dump(self.episode_list, open(f"{path}"), 'wb')
            except:
                return False
        return True


nwc = NaverWebtoonCrawler(651673)
print(nwc.total_episode_count)
