import pymysql
import os
import pickle
import copy
import threading

#profile : id / password / residence / hobby / age / nickname / gender / intro / online / on_chat / vote
#회원table (id_xxx) : 매치 가능성이 있는 회원의 id / is_match  / new_talk / pic1 /pic2 / pic3 / new_profile


#resource_path('./id_' + self.editline_id.text() + '/match/match_candidate_list.txt')

class database():
    def __init__(self):
        self.db = pymysql.connect(host='database-1.cpkdmxea5j3f.ap-northeast-2.rds.amazonaws.com', user='admin', password='12345678', db='project_db', charset='utf8')
        self.curs = self.db.cursor()
        self.result=()
        self.my_dir = os.getcwd()

    def get_data(self,data_list,client_list):
        if data_list[0]=='login_info':
            print('login')
            self.login(data_list,client_list)
        elif data_list[0]=='join_info':
            print('join')
            self.join(data_list)
        elif data_list[0]=='new_profile':
            print('new_profile')
            self.new_profile(data_list)
        elif data_list[0]=='count_users':
            print('count_users')
            return
        elif data_list[0]=='initiate_match':
            print('initiate_match')
            self.get_match_info(data_list)
        elif data_list[0]=='match_like':
            print('match_like')
            self.match_like(data_list)
        elif data_list[0]=='match_pass':
            print('match_pass')
            self.match_pass(data_list)
        elif data_list[0]=='confirm_match_list':
            print('confirm_list')
            self.confirm_match_list(data_list)
        elif data_list[0]=='get_matched':
            print('get_matched')
            self.get_matched(data_list)
        elif data_list[0]=='match_cancel':
            print('match_cancel')
            self.match_cancel(data_list)
        elif data_list[0]=='get_cancel':
            print('get_cancel')
            self.get_cancel(data_list)
        elif data_list[0]=='new_talk':
            print('new_talk')
            self.new_talk(data_list)
        elif data_list[0]=='vote_apply':
            print('vote_apply')
            self.vote_apply(data_list)
        elif data_list[0]=='update_pic':
            print('update_pic')
            self.update_pic(data_list)
        elif data_list[0]=='get_updated_pic':
            print('get_updated_pic')
            self.get_updated_pic(data_list)
        elif data_list[0] == 'get_updated_profile':
            print('get_updated_profile')
            self.get_updated_profile(data_list)
        elif data_list[0] == 'get_profile':
            print('get_profile')
            self.get_profile(data_list)
        elif data_list[0] == 'check_vote':
            print('check_vote')
            self.check_vote(data_list)
        else:
            return

    def login(self,data_list,client_list):
        self.db.commit()
        sql = 'select id,password,online from profile'
        self.curs.execute(sql)
        result = self.curs.fetchall()
        print(1)
        for data in result:
            if data == (data_list[1], data_list[2], 0):
                data_list.insert(1, True)
                print(data_list)
                sql = "update profile set online=1 where id=%s"
                self.curs.execute(sql,(data_list[2],))
                self.db.commit()
                client_list[threading.currentThread()].append(data_list[2])
                return
        data_list.insert(1, False)

    def join(self,data_list):
        print('join1')
        self.db.commit()
        print('join2')
        sql = 'select id from profile'
        print('join3')
        self.curs.execute(sql)
        print('join4')
        result = self.curs.fetchall()
        print('join5')

        for data in result:
            if data[0] == data_list[1]:
                data_list.insert(1, False)
                return

        tmp_list = copy.deepcopy(data_list)
        del(tmp_list[0])
        del(tmp_list[6])
        sql = 'CREATE TABLE id_' + data_list[1] + '( id varchar(50),is_match tinyint not null default 0, new_talk tinyint not null default 0,  pic1 tinyint not null default 0, pic2 tinyint not null default 0, pic3 tinyint not null default 0, new_profile tinyint not null default 0)'
        self.curs.execute(sql)
        self.db.commit()
        if data_list[7] == '남성':
            self.db.commit()
            sql = "select id from profile where gender='여성'"
            self.curs.execute(sql)
            self.result = self.curs.fetchall()
            for i in self.result:
                sql = "insert into id_"+ data_list[1] +" values (%s ,0,0,0,0,0,0)"
                print(sql)
                self.curs.execute(sql,i[0])
            self.db.commit()
        else:
            self.db.commit()
            sql = 'select id from profile where gender="남성"'
            self.curs.execute(sql)
            self.result = self.curs.fetchall()
            for i in self.result:
                sql = "insert into id_" + data_list[1] + " values (%s,0,0,0,0,0,0)"
                print(sql)
                self.curs.execute(sql,i[0])
            self.db.commit()

        sql = 'insert into profile values (%s, %s, %s, %s ,%s, %s, %s, %s, 0, 0, 0)'
        self.curs.execute(sql, (data_list[1], data_list[2], data_list[3], data_list[4], data_list[5],data_list[6],data_list[7],data_list[8]))
        self.db.commit()
        data_list.insert(1, True)
        self.mkdir(data_list)
        f = open('./id_' + tmp_list[0] + '/my_profile.txt', 'wb')
        f.write(pickle.dumps(tmp_list))
        f.close()
        print('profile created')

    #['new_profile', profile_list, 매치리스트]
    # my_profile.txt = [ 내id, 비밀번호, 거주지, 취미, 나이, 닉네임, 성별, 자기소개 ]
    def new_profile(self,data_list):
        fwrite = open('./id_' + data_list[1][0] + '/my_profile.txt','wb')
        fwrite.write(pickle.dumps(data_list[1]))
        fwrite.close()
        sql='update profile set password=%s, residence=%s, hobby=%s, age=%s, nickname=%s,intro=%s  where id=%s'
        self.curs.execute(sql,(data_list[1][1],data_list[1][2],data_list[1][3],data_list[1][4],data_list[1][5],data_list[1][7],data_list[1][0]))
        for item in data_list[2]:
            self.db.commit()
            sql = "select is_match from id_"+data_list[1][0]+" where id='"+item+"'"
            self.curs.execute(sql)
            result = self.curs.fetchall()
            if result[0]:
                sql = "update id_"+item+" set new_profile=1 where id='"+data_list[1][0]+"'"
                self.curs.execute(sql)
                self.db.commit()

    # [ 'get_profile' ,내 id, 프로필을 받아갈 id ]
    def get_profile(self, data_list):
        self.db.commit()
        sql = "select id,is_match from id_" + data_list[1] + " where id='" + data_list[2] + "'"
        self.curs.execute(sql)
        result = self.curs.fetchall()
        print(result)
        if result:
            if result[0][1] == 0:
                sql = "update id_" + data_list[1] + " set is_match=1 where id='" + data_list[2] + "'"
                self.curs.execute(sql)

                # profile = [ 닉네임, 거주지, 취미, 나이, 성별, 자기소개 ]
                self.db.commit()
                sql = "select nickname,residence,hobby,age,gender,intro from profile where id='" + data_list[2] + "'"
                self.curs.execute(sql)
                result2 = self.curs.fetchall()[0]
                data_list.insert(1, True)
                data_list.append(result2)

            else:
                data_list.insert(1, False)
                data_list.append([])
        else:
            # profile = [ 닉네임, 거주지, 취미, 나이, 성별, 자기소개 ]
            self.db.commit()
            sql = "select nickname,residence,hobby,age,gender,intro from profile where id='" + data_list[2] + "'"
            self.curs.execute(sql)
            result = self.curs.fetchall()[0]
            data_list.append(result)
            data_list.insert(1, True)

            sql = "insert into id_" + data_list[2] + " values('" + data_list[3] + "',1,0,0,0,0,0)"
            self.curs.execute(sql)
            self.db.commit()

    def mkdir(self,data_list):
        print(data_list)
        dir_path = self.my_dir + '/id_' + data_list[2]
        try:
            if not (os.path.isdir(dir_path)):
                os.makedirs(os.path.join(dir_path))
            if not (os.path.isdir(dir_path+'/match')):
                os.makedirs(os.path.join(dir_path+'/match'))

        except OSError:
            print('failed to mkdir' + data_list[1])

    # 클라이언트로 보내는 msg_list = ['initiate_match', True, 내id ,[id, nickname , residence ,hobby , age , gender, intro]] or ['initiate_match',False ,id]
    def get_match_info(self,data_list):
        self.db.commit()
        sql = 'select gender from profile where id=%s'
        self.curs.execute(sql,(data_list[1],))
        gender = self.curs.fetchall()[0][0]

        self.db.commit()
        sql = "select id from profile where gender!='"+gender+"' and id not in (select id from id_"+data_list[1]+")"
        print(sql)
        self.curs.execute(sql)
        new_id_list = self.curs.fetchall()

        if len(new_id_list):
            for i in new_id_list:
                sql = "insert into id_" + data_list[1] + " values ('"+ i[0] +"',0,0,0,0,0,0)"
                print(sql)
                self.curs.execute(sql)
                self.db.commit()

        self.db.commit()
        sql = 'select id,nickname,residence,hobby,age,gender,intro from profile where id in (select id from id_'+data_list[1]+' where is_match=0)'
        self.curs.execute(sql)
        match_list = self.curs.fetchall()
        print(match_list)
        if not len(match_list):
            data_list.insert(1,False)
            return

        # 매치될 수 있는 리스트중 아무나 한명 선택 ,리스트는 [ id, nickname , residence ,hobby , age ,intro]
        print(match_list[0])
        data_list.insert(1,True)
        data_list.append(match_list[0])

    def match_like(self,data_list):
        sql = "update id_"+data_list[1]+" set is_match=1 where id=%s"
        self.curs.execute(sql,(data_list[2]))
        self.db.commit()

    def match_pass(self,data_list):
        sql = "update id_"+data_list[1]+" set is_match=-1 where id=%s"
        self.curs.execute(sql, (data_list[2],))
        self.db.commit()

    #[['confirm_match_list', 내id, 내가 like한사람(is_match=1)의 list]
    def confirm_match_list(self,data_list):
        confirmed_list = []
        for item in data_list[2]:
            #상대id, 내id
            self.db.commit()
            sql = "select is_match from id_"+item+" where id='"+data_list[1]+"'"
            self.curs.execute(sql)
            match = self.curs.fetchall()
            if match:
                print(f'match:{match}')
                print(item)
                if match[0][0]==1:
                    confirmed_list.append(item)
        if len(confirmed_list):
            for item in confirmed_list:
                sql = "update id_"+data_list[1]+" set is_match=2 where id='"+item+"'"
                self.curs.execute(sql)
                sql = "update id_"+item+" set is_match=2 where id='"+data_list[1]+"'"
                self.curs.execute(sql)
                print(item)
            print(confirmed_list)
            self.db.commit()
            ## [ 'confirm_match_list',True or False, 매치 성공_list(is_match=2, false이면 빈 리스트), 내 id, 나의like_list ]
            data_list.insert(1,True)
        else:
            data_list.insert(1,False)

        data_list.insert(2,confirmed_list)

    # ['get_matched',내id,내 match_list]
    def get_matched(self,data_list):
        self.db.commit()
        sql = 'select id from id_'+data_list[1]+' where is_match=2'
        self.curs.execute(sql)
        result = self.curs.fetchall()
        send_list = []
        if result:
            for item in result:
                if item[0] in data_list[2]:
                    pass
                else:
                    send_list.append(item[0])
            if send_list:
                data_list.insert(1,True)
            else:
                data_list.insert(1,False)
        else:
            data_list.insert(1,False)
        data_list.insert(2, send_list)

    # ['get_cancel',내id,내 match_list]
    def get_cancel(self,data_list):
        #제대로 체크가 이루어지는 확인
        self.db.commit()
        sql = 'select id from id_'+data_list[1]+' where is_match=-1'
        print(sql)
        self.curs.execute(sql)
        result = self.curs.fetchall()
        print(result)
        cancel_list = []
        if result:
            for item in result:
                if item[0] in data_list[2]:
                    cancel_list.append(item[0])
            if cancel_list:
                data_list.insert(1,True)
            else:
                data_list.insert(1,False)
        else:
            data_list.insert(1, False)

        data_list.insert(2, cancel_list)
        # ['get_cancel',True or False,매치취소된 목록(is_match=2였다가 -1이됨),내id, 보낸 match_list]

    # ['match_cancel', 내id, 매치취소할id]
    def match_cancel(self,data_list):
        sql = "update id_"+data_list[1]+" set is_match=-1 where id='"+data_list[2]+"'"
        self.curs.execute(sql)
        sql = "update id_"+ data_list[2]+" set is_match=-1 where id='" + data_list[1] + "'"
        self.curs.execute(sql)
        self.db.commit()
        data_list.insert(1,True)

    def new_talk(self,data_list):
        self.db.commit()
        sql = "select new_talk from id_"+data_list[1]+" where id='"+data_list[2]+"'"
        self.curs.execute(sql)
        result = self.curs.fetchall()
        if result:
            if result[0][0] == 1:
                sql = "update id_"+data_list[1]+" set new_talk=0 where id='"+data_list[2]+"'"
                self.curs.execute(sql)
                self.db.commit()

                fread = open('./id_' + data_list[1]+'/match/id_'+data_list[2]+'.txt','rb')
                data_read = fread.read()
                fread.close()
                data_list.insert(1,True)
                data_list.insert(2,len(data_read))
            else:
                data_list.insert(1,False)
        else:
            data_list.insert(1,False)

    def vote_apply(self,data_list):
        sql = "update profile set vote ="+str(data_list[2])+" where id='"+data_list[1]+"'"
        self.curs.execute(sql)
        self.db.commit()
        data_list.insert(1,True)

    # ['update_pic', 내 id, 내 매치 리스트, 업데이트한 사진 인덱스]
    def update_pic(self,data_list):
        for item in data_list[2]:
            sql = "update id_"+item+" set pic"+str(data_list[3])+"=1 where is_match=2 and id='"+data_list[1]+"'"
            self.curs.execute(sql)
            self.db.commit()
            print(sql)
            print(f'{item} done')
        data_list.insert(1,True)

    # ['get_updated_pic', 내id, [내 매치 리스트]]
    def get_updated_pic(self,data_list):
        list3 = []
        for item in data_list[2]:
            list1 = []
            list2 = []
            self.db.commit()
            sql = "select pic1,pic2,pic3 from id_"+data_list[1]+" where id='"+item+"'"
            self.curs.execute(sql)
            result = self.curs.fetchall()
            i = 1
            print(result[0])
            if result:
                for index in result[0]:
                    if index == 1:
                        list2.append(i)
                        sql2 = "update id_"+data_list[1]+" set pic"+str(i)+"=0 where id='"+item+"'"
                        self.curs.execute(sql2)
                        self.db.commit()
                    i = i + 1
            if list2:
                list1.append(item)
                list1.append(list2)
                list3.append(list1)
        if list3:
            data_list.insert(1,True)
            data_list.append(list3)
        else:
            data_list.insert(1,False)
            data_list.append(list3)

    # ['get_updated_profile', 내id, [내 매치 리스트]]
    def get_updated_profile(self,data_list):
        list2 = []
        for item in data_list[2]:
            list1 = []
            self.db.commit()
            sql = "select new_profile from id_" + data_list[1] + " where id='" + item + "'"
            self.curs.execute(sql)
            result = self.curs.fetchall()
            if result:
                if result[0][0] == 1:
                    sql = "update id_"+data_list[1]+" set new_profile=0 where id='"+item+"'"
                    self.curs.execute(sql)
                    self.db.commit()
                    fread = open('./id_'+item+'/my_profile.txt','rb')
                    list_read = pickle.loads(fread.read())
                    fread.close()
                    list1.append(item)
                    list1.append(list_read)
            if list1:
                list2.append(list1)
        if list2:
            data_list.insert(1,True)
            data_list.insert(4,list2)
        else:
            data_list.insert(1,False)
            data_list.insert(4,[])

    def check_vote(self,data_list):
        self.db.commit()
        sql = "select vote from profile where id='"+data_list[1]+"'"
        self.curs.execute(sql)
        result = self.curs.fetchall()

        # ['check_vote',True or False, 내id]
        if result[0][0] == 0:
            data_list.insert(1,False)
        else:
            data_list.insert(1,True)

