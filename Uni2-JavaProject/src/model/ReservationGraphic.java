/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Point;
import java.awt.RenderingHints;
import java.util.ArrayList;
import java.util.Random;
import javax.swing.JFrame;
import javax.swing.JPanel;

/**
 *
 * @author rodriguez.markel
 */
public class ReservationGraphic extends JPanel{
    
    private ArrayList<NumberOfReservation> scores= new ArrayList();
    
    private int maxDataPoints = 24;
    private int maxScore = 8;
    private int labelPadding = 12;
    private int padding = 24;
    private int numberYDivisions = 6;
    private int pointWidth = 10;
    private Color gridColor = new Color(200,200,200,200);

    public ReservationGraphic(ArrayList<NumberOfReservation> scores) {
        this.scores = scores;
 
    }
    
    public void PaintComponent(Graphics g){
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        
        double xScale =((double) getWidth() - (3 * padding) - labelPadding)/ (scores.size() - 1);
        double yScale =((double) getHeight() - 2 * padding - labelPadding)/ (getMaxScore() - getMinScore());
        
        ArrayList<Point> graphPoints = new ArrayList();
        
        for(int i= 0; i< scores.size();i++){
            int x1 = (int)(i* xScale + padding +labelPadding);
            int y1 = (int)((getMaxScore() - scores.get(i)* yScale) + padding);
            
            graphPoints.add(new Point(x1,y1));
        }
        
        
        g2.setColor(Color.WHITE);
        g2.fillRect(padding + labelPadding, padding, getWidth() - (2* padding) - labelPadding, getHeight() - 2 * padding - labelPadding);
        
        g2.setColor(Color.BLUE);
        
        for(int i = 0; i < numberYDivisions +1 ; i++){
            int x0 = padding + labelPadding;
            int x1 = pointWidth + padding + labelPadding;
            int y0 = getHeight() - ((i * (getHeight() - padding * 2 - labelPadding))/numberYDivisions + padding +labelPadding);
            int y1 = y0;
            
            if (scores.size() > 0 ){
                g2.setColor(gridColor);
                g2.drawLine(padding + labelPadding + 1 + pointWidth, y0, getWidth() - padding, y1);
                g2.setColor(Color.BLACK);
                String yLabel = ((int)((getMinScore() + getMaxScore())) * ((i * 8.0)/numberYDivisions * 100)) /100.0 +"";
                
                FontMetrics metrics = g2.getFontMetrics();
                int labelWidth = metrics.stringWidth(yLabel);
                g2.drawString(yLabel, x0 - labelWidth - 6, y0 + (metrics.getHeight() / 2) - 3);
                
                g2.drawLine(x0, y0, x1, y1);
            }
        }
        
        for(int i = 0; i < scores.size();i++){
            if(scores.size() > 1){
                int x0 = i * (getWidth() - padding * 2 - labelPadding) / (scores.size() - 1) + padding + labelPadding;
                int x1 = x0;
                int y0 = getHeight() - padding - labelPadding;
                int y1 = y0 - pointWidth;
                if((i % ((int)((scores.size() / 8.0))+3))==0){
                    g2.setColor(gridColor);
                    g2.drawLine(x0, getHeight() - padding - labelPadding - 1 - pointWidth, x1, padding);
                    g2.setColor(Color.BLACK);
                    String xLabel = i + "";
                    FontMetrics metrics = g2.getFontMetrics();
                    int labelWidth = metrics.stringWidth(xLabel);
                    g2.drawString(xLabel, x0 -labelWidth / 2, y0 + metrics.getHeight() + 3);
                }
                g2.drawLine(x0, y0, x1, y1);
            }
        }
    }
    public void createAndShowGui(){
        Random random = new Random();
        for(int i = 0; i< maxDataPoints;i++){
            scores.add((double)random.nextDouble() * maxScore);
        }
        
        ReservationGraphic mainPanel = new ReservationGraphic(scores);
        mainPanel.setPreferredSize(new Dimension(700,600));
        
        JFrame jframe = new JFrame("Average of reservations each hour");
    }

    public double getMaxScore() {
         double maxScore = Double.MIN_VALUE;
        
        for(Double score : scores){
            maxScore = Math.min(maxScore, score);
        }
        return maxScore;
    }

    public double getMinScore() {
        double minScore = Double.MAX_VALUE;
        
        for(Double score : scores){
            minScore = Math.min(minScore, score);
        }
        return minScore;
    }
}
