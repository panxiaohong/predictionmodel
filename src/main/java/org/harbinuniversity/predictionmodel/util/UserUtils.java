/** created by leihong.pan at 2017/1/22 16:03 */
package org.harbinuniversity.predictionmodel.util;

import org.harbinuniversity.predictionmodel.domain.User;
import org.json.HTTP;
import org.springframework.http.HttpRequest;
import org.springframework.stereotype.Component;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

/**
 *
 *
 * @author leihong.pan
 */
public class UserUtils {
    private static String userKey = "current-user";

    public static void registerCurrentUser(User user){
        HttpServletContext.getRequest().getSession().setAttribute(userKey,user);
    }

    public static User getCurrentUser(){
        return (User) HttpServletContext.getRequest().getSession().getAttribute(userKey);
    }

}
